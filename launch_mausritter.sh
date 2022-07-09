#!/bin/bash

if [ -z $PYTHONPATH ]; then
	export PYTHONPATH=$PWD
else
	export PYTHONPATH=$PYTHONPATH:$PWD
fi
python mausritter/mausritter_helper.py