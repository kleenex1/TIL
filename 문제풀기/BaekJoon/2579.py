import sys

sys.stdin = open("_계단오르기.txt")

N = int(input())
scores = [int(input()) for _ in range(N)]
dp = [0]*300

if N == 1:
    print(scores[0])
if N == 2:
    print(sum(scores))
if N == 3:
    print(max(scores[0]+scores[2], scores[1]+scores[2]))
if N > 3:
    dp[0] = scores[0]
    dp[1] = max(scores[0]+scores[1], scores[1])
    dp[2] = max(scores[0]+scores[2], scores[1]+scores[2])

    for i in range(3,N):
        dp[i] = max(dp[i-2]+scores[i], dp[i-3]+scores[i-1]+scores[i])

    print(dp[N-1])  
