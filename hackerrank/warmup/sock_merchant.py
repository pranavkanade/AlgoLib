#!/usr/bin/python3
from pprint import pprint
num_ele = int(input())
inp_list = list(map(int, input().split()))
test_dir = {}
tot = 0
for i in inp_list:
    if i not in test_dir.keys():
        test_dir[i] = 1
    else:
        test_dir[i] += 1
        if test_dir[i] % 2 == 0:
            tot += 1
            test_dir[i] = 0

print(tot)
