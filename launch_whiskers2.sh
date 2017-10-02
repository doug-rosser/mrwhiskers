#!/bin/bash

for x in `seq 11 20`
  do
    su user$x -c "nohup /tmp/mrwhiskers.py &"
  done
