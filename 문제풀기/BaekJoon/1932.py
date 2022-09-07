import sys

sys.stdin = open("_정수삼각형.txt")

N = int(input())

dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1,N):
    for j in range(0,i+1):
        if j == 0:
            dp[i][0] += dp[i-1][0]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(dp)
print(max(dp[N-1]))