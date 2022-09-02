import sys

sys.stdin = open("_거스름돈.txt")

N = int(input())

left = 1000-N
coins = [500,100,50,10,5,1]
cnt = 0
for coin in coins:
    cnt += left//coin
    left %= coin

print(cnt)