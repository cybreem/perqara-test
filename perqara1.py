#!/bin/python3

import math
import os
import random
import re
import sys

def notif(expenditure, d):
    start = 0
    end = d
    counts = [0] * (200+1)
    for val in expenditure[start:end]:
        counts[val] += 1
    n = len(expenditure)
    num_notifications = 0
    while end < n:
        if expenditure[end] >= 2 * center(counts, d):
            num_notifications += 1
        counts[expenditure[start]] -= 1
        counts[expenditure[end]] += 1
        start += 1
        end += 1
    return num_notifications

def center(counts, d):
    total = 0
    half = d / 2
    for i, count in enumerate(counts):
        total += count
        if total > half:
            return i
        if total == half:
            for j in range(i + 1, len(counts)):
                if counts[i] > 0:
                    return (i + j) / 2

print('Input:')
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])

expenditure = list(map(int, input().rstrip().split()))

result = notif(expenditure, d)

print('Output:\n'+str(result) + '\n')
