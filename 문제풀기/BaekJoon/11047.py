import sys

sys.stdin = open("_동전0.txt")

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0
for coin in coins[::-1]:
    count += (K//coin)

    K %= coin

print(count)