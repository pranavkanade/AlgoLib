#!/Users/pskanade/miniconda3/bin/python

s = input()
n = int(input())

# find which is greater
t = len(s)
q = 0
r = 0
tot = 0
if t <= n:
    r = n % t
    q = n // t
else:
    r = n

# count till r
rdash = 0
for lett in s[:r]:
    if lett == 'a':
        rdash += 1
# count after r
qdash = 0
for lett in s[r:]:
    if lett == 'a':
        qdash += 1
tot = (qdash * q) + (rdash * (q+1))

print(tot)
