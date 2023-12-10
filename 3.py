#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

inputfile = "./inputs/3.txt"

# part 1
coord_nums = []
coord_symb = []
for i, line in enumerate(open(inputfile).read().strip().split("\n")):
    nums = re.finditer(r'\d+', line)
    for n in nums:
        coord = []
        for j in range(len(n.group())):
            coord.append((i, n.start() + j))
        coord_nums.append([n.group(), coord])
    symb = re.finditer(r'[^.\d]', line)
    for s in symb:
        coord_symb.append([s.group(), (i, s.start())])

ok = []
tot = 0
for n in coord_nums:
    for c in n[1]:
        for s in coord_symb:
            if abs(c[0] - s[1][0]) <= 1:
                if abs(c[1] - s[1][1]) <= 1:
                    if n not in ok:
                        ok.append(n)
                        tot += int(n[0])
                        break
print(f"Part1: {tot}")

# part 2
coord_symb = [c for c in coord_symb if c[0] == "*"]
coord_symb = [[c[0], c[1], []] for c in coord_symb]

for n in coord_nums:
    for c in n[1]:
        for s in coord_symb:
            if abs(c[0] - s[1][0]) <= 1:
                if abs(c[1] - s[1][1]) <= 1:
                    if int(n[0]) not in s[2]:
                        s[2].append(int(n[0]))
                        break

print('Part2:', sum([s[2][0] * s[2][1] for s in coord_symb if len(s[2]) == 2]))
