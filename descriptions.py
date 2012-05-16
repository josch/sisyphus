import sys
from util import xmlfiletodict, get_articles

def main():
    if len(sys.argv) != 2:
        print "usage:", sys.argv[0], "order.xml"
        exit(1)

    orderline = xmlfiletodict(sys.argv[1])

    for article in get_articles(orderline):
        print '\t'.join([str(a) for a in [
            article['Article']['Description'],
            article['Article']['ID'],
            article['Article']['Type'],
            article['Article']['Family'],
            article['Article']['Length'],
            article['Article']['Width'],
            article['Article']['Height'],
            article['Article']['Weight']]])

if __name__ == "__main__":
    main()
