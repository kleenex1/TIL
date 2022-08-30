import sys

sys.stdin = open("_설탕배달.txt")

N = int(input())
sugar = [3,5]

d = [5001]*(N+1)
d[0] = 0
for i in range(2):
    for j in range(sugar[i], N+1):
        if d[j-sugar[i]] != 5001:
            d[j] = min(d[j], d[j-sugar[i]]+1)

if d[N] == 5001:
    print(-1)
else:
    print(d[N])