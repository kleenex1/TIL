import sys

sys.stdin = open("_LCS.txt")

A = list(input())
B = list(input())

A_list, B_list = len(A), len(B)

dp = [0] * B_list
for i in range(A_list):
    cnt = 0
    for j in range(B_list):
        if cnt < dp[j]:
            cnt = dp[j]
        elif A[i] == B[j]:
            dp[j] = cnt + 1

print(max(dp))