import sys
from util import xmlfiletodict

if len(sys.argv) != 2:
    print "usage:", sys.argv[0], "packlist.xml"
    exit(1)

d = xmlfiletodict(sys.argv[1])

pallets = d["Response"]["PackList"]["PackPallets"]["PackPallet"]

if not isinstance(pallets, list):
    pallets = [pallets]

num_articles = 0

for pallet in pallets:
    num_articles += len(pallet["Packages"]["Package"])

print num_articles
