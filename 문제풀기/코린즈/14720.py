import sys

sys.stdin = open("_우유축제.txt")

N = int(input())
S = list(map(int, input().split()))

cnt = 0
for i in S:
    if cnt % 3 == i:
        cnt += 1

print(cnt)