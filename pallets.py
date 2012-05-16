import sys
from util import xmlfiletodict, get_articles

def main():
    if len(sys.argv) != 2:
        print "usage:", sys.argv[0], "order.xml"
        exit(1)

    d = xmlfiletodict(sys.argv[1])

    pallets = d['Message']['PalletInit']['Pallets']['Pallet']

    if not isinstance(pallets, list):
        pallets = [pallets]

    for p in pallets:
        print "\t".join([
            p['Dimensions']['Length'],
            p['Dimensions']['Width'],
            p['Dimensions']['MaxLoadHeight'],
            p['Dimensions']['MaxLoadWeight']
            ])

if __name__ == "__main__":
    main()
