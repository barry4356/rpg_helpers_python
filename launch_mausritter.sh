#!/bin/bash

if [ -z $PYTHONPATH ]; then
	export PYTHONPATH=$PWD:${PWD}/mausritter:${PWD}/mausritter/tables:${PWD}/common
else
	export PYTHONPATH=$PYTHONPATH:$PWD:${PWD}/mausritter:${PWD}/mausritter/tables:${PWD}/common
fi
clear
python mausritter/mausritter_main.py
