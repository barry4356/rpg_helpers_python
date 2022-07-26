#!/bin/bash

if [ -z $PYTHONPATH ]; then
	export PYTHONPATH=$PWD:${PWD}/mausritter:${PWD}/mausritter/tables:${PWD}/common
else
	export PYTHONPATH=$PYTHONPATH:$PWD:${PWD}/mausritter:${PWD}/mausritter/tables:${PWD}/common
fi
clear
if [ "$#" -eq 1 ]; then
  if [ "${1}" = "-t" ]; then
    python -c 'import mausritter_main; mausritter_main.mausritter_terminal()'
  else
    python mausritter/mausritter_main.py
  fi
else
  python mausritter/mausritter_main.py
fi
