#!/bin/bash

if [ -z $PYTHONPATH ]; then
	export PYTHONPATH=$PWD:${PWD}/../:${PWD}/../../common:${PWD}/../tables
else
	export PYTHONPATH=$PYTHONPATH:$PWD/../:$PWD:${PWD}/../.../common:${PWD}/../tables
fi
echo "Testing Dungeon Tools..."
python dungeon_test.py > dungeon_test.txt
