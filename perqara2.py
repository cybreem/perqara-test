#!/bin/python3

import math
import os
import random
import re
import sys

def visible(size, rowQueen, colQueen, obstacles):
    count = 0
    smallest_distances = direction_move(size, rowQueen, colQueen)
    for obs in obstacles:
        direction, distance = obstacle(rowQueen, colQueen, *obs)
        distance -= 1
        if direction:
            smallest_distances[direction] = min(distance, smallest_distances[direction])
            
    count = sum(smallest_distances.values())
    return count

def direction_move(size, rowQueen, colQueen):
    d = {}
    d['n'] = size - rowQueen
    d['s'] = rowQueen - 1
    d['e'] = size - colQueen
    d['w'] = colQueen - 1
    d['ne'] = min(d['n'], d['e'])
    d['nw'] = min(d['n'], d['w'])
    d['se'] = min(d['s'], d['e'])
    d['sw'] = min(d['s'], d['w'])
    
    return d

def obstacle(rowQueen, colQueen, ro, co):
    if rowQueen == ro:
        if co < colQueen:
            return 'w', colQueen - co
        elif co > colQueen:
            return 'e', co - colQueen
    if colQueen == co:
        if ro < rowQueen:
            return 's', rowQueen - ro
        elif ro > rowQueen:
            return 'n', ro - rowQueen
    if ro - rowQueen == co - colQueen:
        if ro < rowQueen:
            return 'sw', rowQueen - ro
        elif ro > rowQueen:
            return 'ne', ro - rowQueen
    if ro - rowQueen == colQueen - co:
        if ro < rowQueen:
            return 'se', rowQueen - ro
        elif ro > rowQueen:
            return 'nw', ro - rowQueen
    return '', -1

print('Input:')
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rowQueen,colQueen = input().strip().split()
rowQueen,colQueen = [int(rowQueen),int(colQueen)]
obstacles = []
for _ in range(k):
    rowObstacle,colObstacle = input().strip().split()
    rowObstacle,colObstacle = [int(rowObstacle),int(colObstacle)]
    obstacles.append((rowObstacle, colObstacle))
print('Output:')
print(visible(n, rowQueen, colQueen, obstacles))
