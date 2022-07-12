#!/bin/bash

if [ -z $PYTHONPATH ]; then
	export PYTHONPATH=$PWD:${PWD}/mausritter:${PWD}/mausritter/tables
else
	export PYTHONPATH=$PYTHONPATH:$PWD:${PWD}/mausritter:${PWD}/mausritter/tables
fi
clear
python mausritter/mausritter_main.py
