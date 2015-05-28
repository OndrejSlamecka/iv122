#!/usr/bin/env bash

for i in {1..4}; do
	cat "maze$i.txt" | ./weighted_maze.py | dot -Tpng -o "maze$i.png";
done
