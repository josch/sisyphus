import sys
import subprocess
import itertools
from util import dicttoxmlfile, get_packlist_dict, get_packlist_dict_multi, dicttoxmlstring, get_order_dict
from arrange_spread2 import arrange_in_layer
import cPickle
from binascii import a2b_base64
import tempfile
import os
import zlib
import fcntl
import ctypes

libpallet = ctypes.cdll.LoadLibrary('./libpallet.so.0.0.0')
libpallet.evaluate.restype = ctypes.c_double

if os.environ.get("multi_pallet"):
    try_multi_pallet = bool(int(os.environ["multi_pallet"]))
else:
    try_multi_pallet = False

if os.environ.get("permutations"):
    try_permutations = bool(int(os.environ["permutations"]))
else:
    try_permutations = True

def pack_single_pallet(permut_layers, rest_layers, pallet):
    pack_sequence = 1
    pack_height = 0

    articles_to_pack = list()

    for layer in list(permut_layers)+rest_layers:
        pack_height += layer[0]['Article']['Height']
        #if pack_height > pallet['Dimensions']['MaxLoadHeight']:
        #    break
        for article in layer:
            article['PackSequence'] = pack_sequence
            article['PlacePosition']['Z'] = pack_height
            articles_to_pack.append(article)
            pack_sequence += 1

    return get_packlist_dict(pallet, articles_to_pack)

def pack_multi_pallet(permut_layers, rest_layers, pallet):
    sum_all_article_height = sum([layer[0]['Article']['Height'] for layer in list(permut_layers)+rest_layers])

    number_of_pallets = int(sum_all_article_height/pallet['Dimensions']['MaxLoadHeight'])+1

    article_lists = [ list() for i in range(number_of_pallets) ]
    pack_heights = [ 0 for i in range(number_of_pallets) ]
    pack_sequences = [ 1 for i in range(number_of_pallets) ]

    # spread over pallets in order
    for layer in list(permut_layers)+rest_layers:
        # select as current, the pallet with the lowest height
        current_pallet = pack_heights.index(min(pack_heights))
        pack_heights[current_pallet] += layer[0]['Article']['Height']
        for article in layer:
            article['PackSequence'] = pack_sequences[current_pallet]
            article['PlacePosition']['Z'] = pack_heights[current_pallet]
            article_lists[current_pallet].append(article)
            pack_sequences[current_pallet] += 1

    return get_packlist_dict_multi(pallet, article_lists)

def evaluate_single_pallet(packlist):
    tmp_fh, tmp = tempfile.mkstemp()
    dicttoxmlfile(packlist, tmp)
    result = libpallet.evaluate(sys.argv[1], tmp, sys.argv[3])
    os.close(tmp_fh)
    os.remove(tmp)
    return result

def evaluate_multi_pallet(packlist):
    pallets = packlist['Response']['PackList']['PackPallets']['PackPallet']

    article_lists = [ pallet['Packages']['Package'] for pallet in pallets ]

    scores = list()
    for pallet, articles_to_pack in zip(pallets, article_lists):
        partial_packlist = get_packlist_dict(pallet, articles_to_pack)
        tmp_fh, tmp = tempfile.mkstemp()
        tmp_order_fh, tmp_order = tempfile.mkstemp()
        dicttoxmlfile(partial_packlist, tmp)
        dicttoxmlfile(get_order_dict(pallet, articles_to_pack), tmp_order)
        scores.append(libpallet.evaluate(tmp_order, tmp, sys.argv[3]))
        os.close(tmp_fh)
        os.close(tmp_order_fh)
        os.remove(tmp)
        os.remove(tmp_order)

    return sum(scores)/len(scores)

def evaluate_layers_rests(layers, rests, score_max, pallet, result_max):
    rest_layers = list()
    # sort rests by space they cover and move them to the center of the pile
    # append them to the layer list
    for rest in sorted(rests, key=lambda rest: sum([article['Article']['Length']*article['Article']['Width'] for article in rest]), reverse=True):
        plength, pwidth = (pallet['Dimensions']['Length'], pallet['Dimensions']['Width'])
        root, layer, rest = arrange_in_layer(rest, plength, pwidth)

        com_x = 0
        com_y = 0
        for article in layer:
            com_x += article['PlacePosition']['X']
            com_y += article['PlacePosition']['Y']
        com_x, com_y = com_x/len(layer), com_y/len(layer)

        diff_x, diff_y = plength*0.5-com_x, pwidth*0.5-com_y

        #TODO: for long/wide layers the center of mass might delta might
        #      create an overhang over one side of the pallet
        for article in layer:
            article['PlacePosition']['X'] += diff_x
            article['PlacePosition']['Y'] += diff_y

        rest_layers.append(layer)

    if try_permutations:
        permutations = itertools.permutations(layers)
    else:
        permutations = [tuple(layers)]
    for permut_layers in permutations:
        if try_multi_pallet:
            packlist = pack_multi_pallet(permut_layers, rest_layers, pallet)
        else:
            packlist = pack_single_pallet(permut_layers, rest_layers, pallet)

        # ugly, ugly, ugly, ugly hack - dont copy this...
        #score = float(subprocess.check_output(sys.argv[3]+" -o "
        #    +sys.argv[1]+" -p "+tmp
        #    +" -s "+sys.argv[4]+" --headless | grep Score", shell=True).split(' ')[1].strip())
        if try_multi_pallet:
            score = evaluate_multi_pallet(packlist)
        else:
            score = evaluate_single_pallet(packlist)
        if score >= score_max[0]:
            result_max[0] = dicttoxmlstring(packlist)
            score_max[0] = score

def main():
    if len(sys.argv) < 5:
        print "usage:", sys.argv[0], "order.xml packlist.xml scoring.xml LAYER [LAYER..]"
        exit(1)

    score_max = [0]
    result_max = [None]
    for arg in sys.argv[4:]:
        layers, rests, pallet = cPickle.loads(zlib.decompress(a2b_base64(arg)))
        evaluate_layers_rests(layers, rests, score_max, pallet, result_max)

    print score_max[0]

    lock = open("score_max.lock", "w")
    fcntl.lockf(lock, fcntl.LOCK_EX)
    if os.path.isfile("score_max"):
        with open("score_max", "r") as f:
            score_max_f = float(f.read())
    else:
        score_max_f = 0.0
    if score_max[0] > score_max_f:
        with open(sys.argv[2], "w+") as f:
            f.write(result_max[0])
        with open("score_max", "w+") as f:
            f.write(str(score_max[0]))
    lock.close()

if __name__ == "__main__":
    main()
