import ctypes, sys
from util import xmlfiletodict, get_packlist_dict, dicttoxmlfile, get_order_dict
import tempfile
import os

if len(sys.argv) != 3:
    print "usage:", sys.argv[0], "packlist.xml scoring.xml"
    exit(1)

libpallet = ctypes.cdll.LoadLibrary('./libpallet.so.0.0.0')
libpallet.evaluate.restype = ctypes.c_double

packlist = xmlfiletodict(sys.argv[1])

pallets = packlist['Response']['PackList']['PackPallets']['PackPallet']

article_lists = [ pallet['Packages']['Package'] for pallet in pallets ]

scores = list()
for pallet, articles_to_pack in zip(pallets, article_lists):
    partial_packlist = get_packlist_dict(pallet, articles_to_pack)
    tmp_fh, tmp = tempfile.mkstemp()
    tmp_order_fh, tmp_order = tempfile.mkstemp()
    dicttoxmlfile(partial_packlist, tmp)
    dicttoxmlfile(get_order_dict(pallet, articles_to_pack), tmp_order)
    scores.append(libpallet.evaluate(tmp_order, tmp, sys.argv[2]))
    os.close(tmp_fh)
    os.close(tmp_order_fh)
    os.remove(tmp)
    os.remove(tmp_order)
    #print tmp_order, tmp
print scores

print sum(scores)/len(scores)
