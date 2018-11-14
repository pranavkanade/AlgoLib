#!/usr/bin/python3

# this is lenghty solution

from pprint import pprint

t = int(input())

for _ in range(t):
    n = int(input())
    q = list(map(int, input().rstrip().split()))

    l = q[0]
    tot = 0
    c = False
    for i in range(n):
        if i < q[i] - 3:
            c = True
            break
    if c:
        print("Too chaotic")
        continue

    for i in range(n):
        for j in range(n-i-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                tot += 1

    print(tot)
