#!/bin/bash

if [ -z $PYTHONPATH ]; then
	export PYTHONPATH=$PWD:${PWD}/../:${PWD}/../../common:${PWD}/../tables
else
	export PYTHONPATH=$PYTHONPATH:$PWD/../:$PWD:${PWD}/../.../common:${PWD}/../tables
fi
python maus_roller_test.py
