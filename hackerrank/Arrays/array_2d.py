#!/usr/bin/python3
from pprint import pprint

n = 6
grid = []
for _ in range(6):
    grid.append(list(map(int, input().rstrip().split())))

temp = []
for i in range(n):
    _temp = []
    for j in range(n-2):
        gi = grid[i]
        _temp.append(gi[j] + gi[j+1] + gi[j+2])
    temp.append(_temp)

res = []
for i in range(len(temp) - 2):
    for j in range(len(temp[0])):
        res.append(temp[i][j] + temp[i+2][j] + grid[i+1][j+1])


print(max(res))
