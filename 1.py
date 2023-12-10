#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

inputfile = "./inputs/1.txt"

# first part
sum = 0
for line in open(inputfile, 'r').readlines():
    fnd = re.findall(r"\d", line)
    sum += int(f'{fnd[0]}{fnd[-1]}')
print(f"Part1: {sum}")

# second part
digs = [str(i) for i in range(1, 10)] + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digs = {i: j+1 if j < 9 else j-8 for j, i in enumerate(digs)}
sum = 0
for line in open(inputfile, 'r').readlines():
    fnd = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
    sum += int(f'{digs[fnd[0]]}{digs[fnd[-1]]}')
print(f"Part2: {sum}")