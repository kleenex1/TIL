import sys

sys.stdin = open("_잃어버린괄호.txt")

ex = input().split('-')
s = 0
for i in ex[0].split('+'):
    s += int(i)

for i in ex[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s) 