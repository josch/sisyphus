import ctypes, sys

if len(sys.argv) != 4:
    print "usage:", sys.argv[0], "order.xml packlist.xml scoring.xml"
    exit(1)

libpallet = ctypes.cdll.LoadLibrary('./libpallet.so.0.0.0')
libpallet.evaluate.restype = ctypes.c_double
print libpallet.evaluate(sys.argv[1], sys.argv[2], sys.argv[3])
