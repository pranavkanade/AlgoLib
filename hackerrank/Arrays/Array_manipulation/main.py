from pprint import pprint

n, ops = list(map(int, input().rstrip().split()))

arr = [0]*n

for o in range(ops):
    i, j, inc = list(map(int, input().rstrip().split()))
    for l in range(i-1, j):
        arr[l] += inc
return(max(arr))