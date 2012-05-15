#!/bin/sh -ex

if [ $# -ne 3 ]; then
	echo usage: $0 order.xml packlist.xml scoring.xml
	exit 1
fi

rm -f score_max

python bruteforce2.py $1 | sort -r | xargs --max-procs=4 --max-args=1 python bruteforce3.py $1 $2 $3

echo palletViewer -o $1 -p $2 -s $3

echo python evaluate.py $1 $2 $3
