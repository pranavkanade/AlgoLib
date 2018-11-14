#!/usr/bin/python3

from pprint import pprint

t = int(input())

for _ in range(t):
    n = int(input())
    q = list(map(int, input().rstrip().split()))

    l = q[0]
    tot = 0
    c = False
    for i in range(n-1, -1, -1):
        if i < q[i] - 3:
            print("Too chaotic")
            c = True
            break 
        # The limit to this loop comes from the condition
        # that states that one can only bribe 2 ppl
        # This means that qi can only move forward to
        # qi-1 and qi-2
        # Hence we can just check for overtakers in the range
        # max(0, qi-2) to i
        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                tot += 1
    if not c:
        print(tot)
