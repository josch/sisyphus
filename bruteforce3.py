import sys
import subprocess
import itertools
import shutil
from util import xmlfiletodict, dicttoxmlfile, get_pallet, get_articles, get_packlist_dict
from arrange_spread2 import arrange_in_layer, spread_articles, find_articles
import cPickle
import marshal
from binascii import a2b_base64
import tempfile
import os

def evaluate_layers_rests(layers, rests, scores, pallet):
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
        score = float(subprocess.check_output("../palletandtruckviewer-3.0/palletViewer -o "
            +sys.argv[1]+" -p "+tmp
            +" -s ../icra2011TestFiles/scoreAsPlannedConfig1.xml --headless | grep Score", shell=True).split(' ')[1].strip())
        scores.append(score)
        if score > max(scores+[0]):
            shutil.move(tmp, sys.argv[2])
        else:
            os.remove(tmp)

def main():
    scores = list()
    for arg in sys.argv[3:]:
        layers, rests, pallet = cPickle.loads(a2b_base64(arg))
        evaluate_layers_rests(layers, rests, scores, pallet)

    print max(scores)
    #print "max:", max(scores)
    #print "min:", min(scores)
    #mean = sum(scores)/len(scores)
    #print "mean:", mean
    #from math import sqrt
    #print "stddev:", sqrt(sum([(x-mean)**2 for x in scores])/len(scores))

if __name__ == "__main__":
    main()
