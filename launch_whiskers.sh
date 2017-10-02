#!/bin/bash

for x in `seq 1 10`
  do
    su user$x -c "nohup /tmp/mrwhiskers.py &"
  done
