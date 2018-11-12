#!/usr/bin/python3

from pprint import pprint

n = int(input())
path = list(map(int, input().rstrip().split()))
tot = 0
i = n - 1
while i in range(n-1, 0, -1):
    if (i-2) >= 0 and path[i-2] == 0:
        i = i - 2
    else:
        i = i - 1
    tot += 1
print(tot)
