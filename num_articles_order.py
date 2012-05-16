import sys
from util import xmlfiletodict, get_pallet, get_articles

if len(sys.argv) != 2:
    print "usage:", sys.argv[0], "order.xml"
    exit(1)

orderline = xmlfiletodict(sys.argv[1])
pallet = get_pallet(orderline)
articles = get_articles(orderline)

print len(articles)
