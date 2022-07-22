#!/bin/bash

if [ -z $PYTHONPATH ]; then
	export PYTHONPATH=$PWD:${PWD}/../:${PWD}/../../common:${PWD}/../tables
else
	export PYTHONPATH=$PYTHONPATH:$PWD/../:$PWD:${PWD}/../.../common:${PWD}/../tables
fi
echo "Testing Encounter Roller..."
python encounter_roller_test.py > results/encounter_test.txt
