import sys

sys.stdin = open("_우유축제.txt")

N = int(input())
S = list(map(int, input().split()))


# 0=딸기우유
# 1=초코우유
# 2=바나나우유 

# cnt = 0
# for i in S:
#     if cnt % 3 == i:
#         cnt += 1 

# print(cnt)
# 7
# 0 1 2 0 1 2 0

dp = {i:[0,0,0] for i in range(N)}
start = S.index(0)
dp[start][0] = 1
print('##############1')
print(dp)
for i in range(start+1,N):
    milk = S[i]
    print('##############2')
    print(milk)
    dp[i] = dp[i-1].copy()
    print('##############3')
    print(dp)
    if dp[i][(milk-1)%3] != 0:
        dp[i][milk] = max(dp[i-1][(milk-1)%3]+1, dp[i-1][milk])
        print('##############4')
        print(dp)

