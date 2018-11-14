#!/usr/bin/python3

from pprint import pprint


nd = input().split()
n = int(nd[0])
d = int(nd[1])

a = list(map(int, input().rstrip().split()))

res = []
res.extend(a[d:])
res.extend(a[:d])
print(" ".join(list(map(str, res))))
