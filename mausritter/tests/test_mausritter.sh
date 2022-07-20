#!/bin/bash

for file in $(find . -name "launch*.sh"); do
  bash ${file}
  echo ""
done
sleep 5
