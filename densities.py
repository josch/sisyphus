import sys
from glob import glob
from util import xmlfiletodict, get_articles

def main():
    if len(sys.argv) != 2:
        print "usage:", sys.argv[0], "order.xml"
        exit(1)

    orderline = xmlfiletodict(sys.argv[1])

    for article in get_articles(orderline):
        volume = article['Article']['Length']*article['Article']['Width']*article['Article']['Height']
        print 1000.0*article['Article']['Weight']/volume

if __name__ == "__main__":
    main()
