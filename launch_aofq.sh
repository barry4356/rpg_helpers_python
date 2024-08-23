#!/bin/bash

if [ -z $PYTHONPATH ]; then
	export PYTHONPATH=$PWD:${PWD}/AoFQ:${PWD}/AoFQ/tables:${PWD}/common
else
	export PYTHONPATH=$PYTHONPATH:$PWD:${PWD}/AoFQ:${PWD}/AoFQ/tables:${PWD}/common
fi

python AoFQ/gen_mission.py "$@"
