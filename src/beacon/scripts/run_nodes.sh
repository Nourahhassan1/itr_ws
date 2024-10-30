#!/bin/bash

roscore &
core_pid=$!

sleep 3

for ((i=1; i<=200; i++))
do
  echo "Iteration $i"

  rosrun turtlesim turtlesim_node & &>/dev/null
  sim_pid=$!

  sleep 1

  rosrun beacon beacon_node.py &
  beacon_pid=$!

  timeout 30 rosrun first_coursework key_finder.py

  kill -15 $sim_pid $beacon_pid 2>/dev/null
  sleep 1

done

kill -15 $core_pid