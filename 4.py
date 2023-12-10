#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

inputfile = "./inputs/4.txt"

# part 1
rslt = 0
for line in open(inputfile, 'r').readlines():
    win, my = re.split(r'[|:] ', line)[1:]
    win = set([n.strip() for n in win.split()])
    my = set([n.strip() for n in my.split()])
    if my.intersection(win):
        rslt += [2 ** (n - 1) for n in range(1, len(my.intersection(win)) + 1)][-1]
print(f"Part1: {rslt}")

# part 2
cntr = 0
cards = [re.split(r'[|:] ', line)[1:] for line in open(inputfile, 'r').readlines()]
cards = [(set(c[0].split()), set(c[1].split())) for c in cards]
cards = [[1, len(c[0].intersection(c[1]))] for c in cards]

for i, c in enumerate(cards):
    cntr += c[0]
    for x in range(c[0]):
        for y in range(c[1]):
            cards[i+y+1][0] += 1
print(f"Part2: {cntr}")