#!/bin/bash

if [ -z $PYTHONPATH ]; then
	export PYTHONPATH=$PWD:${PWD}/../
else
	export PYTHONPATH=$PYTHONPATH:$PWD/../:$PWD
fi
python dice_test.py
