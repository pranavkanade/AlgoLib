#!/usr/bin/python3

n = int(input())
arr = list(map(int, input().rstrip().split()))

place = {arr[i]: i for i in range(n)}

count = 0
for i in range(n):
    if i+1 != arr[i]:
        ai, bi = i, place[i+1]
        at, bt = arr[ai], arr[bi]
        place[at], place[i+1] = place[i+1], place[at]
        arr[ai], arr[bi] = bt, at
        count += 1

print(count)
