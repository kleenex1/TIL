import sys

sys.stdin = open("_수들의합.txt")

N = int(input())

n = 1
answer = n
while n*(n+1)//2 <= N:
    if N - n*(n+1)//2 <= n:
        answer = n
    n += 1

print(answer)


