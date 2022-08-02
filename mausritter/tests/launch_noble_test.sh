#!/bin/bash

if [ -z $PYTHONPATH ]; then
	export PYTHONPATH=$PWD:${PWD}/../:${PWD}/../../common:${PWD}/../tables
else
	export PYTHONPATH=$PYTHONPATH:$PWD/../:$PWD:${PWD}/../.../common:${PWD}/../tables
fi
echo "Testing Nobles Tools..."
python noble_test.py > results/noble_test.txt
rm -rf mausritter
