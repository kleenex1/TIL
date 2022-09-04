import sys

sys.stdin = open("_가장긴증가하는부분수열.txt")

N = int(input())

nums = list(map(int, input().split()))

dp = [1]*N

for i in range(N):
    cnt = 0
    for j in range(i):
        if cnt < dp[j]:
            cnt = dp[j]
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))