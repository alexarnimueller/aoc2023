#! /usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from functools import reduce
from operator import mul

inputfile = "./inputs/2.txt"

# part 1
cubes = {"red": 12, "green": 13, "blue": 14}
sum = 0

for line in open(inputfile).readlines():
    fail = False
    for s in line.split(":")[1].split(";"):
        tot = defaultdict(int)
        for pair in s.strip().split(", "):
            tot[pair.split()[1]] += int(pair.split()[0])
        if any(tot[k] > cubes[k] for k in tot.keys()):
            fail = True
    if not fail:
        sum += int(line.split(":")[0].split()[1])
print(f"Part1: {sum}")

# part 2
sum = 0
for line in open(inputfile).readlines():
    tot = defaultdict(int)
    for s in line.split(":")[1].split(";"):
        for pair in s.strip().split(", "):
            if tot[pair.split()[1]] < int(pair.split()[0]):
                tot[pair.split()[1]] = int(pair.split()[0])
    sum += reduce(mul, list(tot.values()))
print(f"Part2: {sum}")