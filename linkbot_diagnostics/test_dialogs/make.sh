#!/bin/sh

for i in *.ui; do
    pyuic4 $i > `basename -s .ui $i`.py
done
