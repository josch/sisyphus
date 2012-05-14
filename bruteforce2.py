import sys
import itertools
from util import xmlfiletodict, get_pallet, get_articles, product_varlength
from arrange_spread2 import arrange_in_layer, spread_articles
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

def get_bitmask(num, length):
    return tuple(( bool(num>>pos&1) for pos in xrange(length-1,-1,-1) ))

def main():
    if len(sys.argv) != 2:
        print "usage:", sys.argv[0], "order.xml"
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

    product_it = product_varlength(4)
    while True:
        rests = list()
        layers = list()
        try:
            rot_article, rot_pallet = get_bitmask(product_it.send(True), 2) # start a new combination
        except TypeError:
            rot_article, rot_pallet = get_bitmask(product_it.next(), 2) # can't send to a just-started generator
        except StopIteration:
            break # generator empty
        it = get_layers(bins, pallet, rot_article, rot_pallet)
        layer, rest = it.next()
        if layer:
            layers.append(layer)
        if rest:
            rests.append(rest)

        while True:
            try:
                layer, rest = it.send(get_bitmask(product_it.send(False), 2))
                if layer:
                    layers.append(layer)
                if rest:
                    rests.append(rest)
            except StopIteration:
                break
        print b2a_base64(zlib.compress(cPickle.dumps((layers, rests, pallet)))),
if __name__ == "__main__":
    main()
