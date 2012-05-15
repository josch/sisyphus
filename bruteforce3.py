import sys
import subprocess
import itertools
from util import dicttoxmlfile, get_packlist_dict, dicttoxmlstring
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

def evaluate_layers_rests(layers, rests, scores, pallet, result_max):
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

    for permut_layers in itertools.permutations(layers):
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

        packlist = get_packlist_dict(pallet, articles_to_pack)

        _, tmp = tempfile.mkstemp()
        dicttoxmlfile(packlist, tmp)

        # ugly, ugly, ugly, ugly hack - dont copy this...
        #score = float(subprocess.check_output(sys.argv[3]+" -o "
        #    +sys.argv[1]+" -p "+tmp
        #    +" -s "+sys.argv[4]+" --headless | grep Score", shell=True).split(' ')[1].strip())
        score = libpallet.evaluate(sys.argv[1], tmp, sys.argv[3])
        if score >= max(scores+[0]):
            result_max[0] = dicttoxmlstring(packlist)
        os.remove(tmp)
        scores.append(score)

def main():
    if len(sys.argv) < 5:
        print "usage:", sys.argv[0], "order.xml packlist.xml scoring.xml LAYER [LAYER..]"
        exit(1)

    scores = list()
    result_max = [None]
    for arg in sys.argv[4:]:
        layers, rests, pallet = cPickle.loads(zlib.decompress(a2b_base64(arg)))
        evaluate_layers_rests(layers, rests, scores, pallet, result_max)

    print max(scores)
    #print "max:", max(scores)
    #print "min:", min(scores)
    #mean = sum(scores)/len(scores)
    #print "mean:", mean
    #from math import sqrt
    #print "stddev:", sqrt(sum([(x-mean)**2 for x in scores])/len(scores))

    lock = open("score_max.lock", "w")
    fcntl.lockf(lock, fcntl.LOCK_EX)
    if os.path.isfile("score_max"):
        with open("score_max", "r") as f:
            score_max = float(f.read())
    else:
        score_max = 0.0
    if max(scores) > score_max:
        with open(sys.argv[2], "w+") as f:
            f.write(result_max[0])
        with open("score_max", "w+") as f:
            f.write(str(max(scores)))
    lock.close()

if __name__ == "__main__":
    main()
