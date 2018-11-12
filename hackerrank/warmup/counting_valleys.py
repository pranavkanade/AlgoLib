#!/usr/bin/python3
from pprint import pprint

n = int(input())
path = input()

d = 'D'
u = 'U'

going_down = False
going_up = False
test = True
l = len(path)
i = 0
cd = 0
cu = 0
for each_step in path:
    if cd > cu:
        going_down = True
    if each_step == d:
        cd += 1
    else:
        cu += 1
    if cd == cu and going_down:
        cd = 0
        cu = 0
        going_down = False
        i += 1
    elif cd == cu:
        cd = 0
        cu = 0

print(i)
