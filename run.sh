#!/bin/sh -ex

rm -f score_max

VIEWER=../palletandtruckviewer-3.0/palletViewer
SCORING=../icra2011TestFiles/scoreAsPlannedConfig1.xml

python bruteforce2.py $1 \
 | sort\
 | uniq\
 | xargs --max-procs=4 python bruteforce3.py $1 packlist.xml $VIEWER $SCORING
