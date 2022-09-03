import sys

sys.stdin = open("_뒤집기.txt")

N = input()

zero = 0
one = 0

if N[0] == '0':
    one += 1
else:
    zero += 1

for i in range(1, len(N)):
    if N[i-1] != N[i]:
        if N[i] == '1':
            zero += 1
        else:
            one += 1

print(min(zero, one))