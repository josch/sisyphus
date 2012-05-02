import sys
import subprocess
import itertools
import shutil
from util import xmlfiletodict, dicttoxmlfile, get_pallet, get_articles, get_packlist_dict
from arrange_spread2 import arrange_in_layer, spread_articles, find_articles
import cPickle
from binascii import b2a_base64
import zlib

def rotate(node):
    if node is None:
        return

    if node['article']:
        # exchange x and y coordinate
        node['article']['PlacePosition']['X'], node['article']['PlacePosition']['Y'] = node['article']['PlacePosition']['Y'], node['article']['PlacePosition']['X']
        # rotate article
        node['article']['Orientation'] = node['article']['Orientation']%2+1

    rotate(node['right'])
    rotate(node['down'])

def get_layers(bins, pallet, rot_article=False, rot_pallet=False):
    for abin in bins:
        bins[abin] = sorted(bins[abin], key=lambda article: article['Article']['Length']*article['Article']['Width'], reverse=True)
        plength, pwidth = (pallet['Dimensions']['Length'], pallet['Dimensions']['Width'])
        if rot_pallet:
            root, layer, rest = arrange_in_layer(bins[abin], pwidth, plength, rot_article=rot_article)
        else:
            root, layer, rest = arrange_in_layer(bins[abin], plength, pwidth, rot_article=rot_article)
        while layer:
            spread_articles(root)
            if rot_pallet:
                rotate(root)

            occupied_area = 0
            for article in layer:
                length, width = article['Article']['Length'], article['Article']['Width']
                occupied_area += length*width

            # print "layer occupation:", occupied_area/float(plength*pwidth)
            if occupied_area/float(plength*pwidth) <= 0.7:
                rot_article, rot_pallet = (yield None, layer)
            else:
                rot_article, rot_pallet = (yield layer, None)

            if rot_pallet:
                root, layer, rest = arrange_in_layer(rest, pwidth, plength, rot_article=rot_article)
            else:
                root, layer, rest = arrange_in_layer(rest, plength, pwidth, rot_article=rot_article)

def get_bit(num, pos):
    return num>>pos&1

def main():
    if len(sys.argv) != 3:
        print "usage:", sys.argv[0], "order.xml packlist.xml"
        exit(1)

    orderline = xmlfiletodict(sys.argv[1])
    pallet = get_pallet(orderline)
    articles = get_articles(orderline)
    bins = dict()

    for article in articles:
        abin = bins.get(article['Article']['Height'])
        if abin:
            abin.append(article)
        else:
            bins[article['Article']['Height']] = [article]

    scores = list()

    stuff1 = list()

    for order in itertools.product([0,1,2,3], repeat=8):
    #for order in [[True]*12,]:
        rests = list()
        layers = list()

        it = get_layers(bins, pallet, get_bit(order[0], 0), get_bit(order[0], 1))
        layer, rest = it.next()
        if layer:
            layers.append(layer)
        if rest:
            rests.append(rest)

        fail = True
        for rot_article in order[1:]:
            try:
                layer, rest = it.send((get_bit(rot_article,0), get_bit(rot_article,1)))
                if layer:
                    layers.append(layer)
                if rest:
                    rests.append(rest)
            except StopIteration:
                fail = False
                break
        if fail:
            raise Exception("finished early")
        print b2a_base64(zlib.compress(cPickle.dumps((layers, rests, pallet)))),
if __name__ == "__main__":
    main()
