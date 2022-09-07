import sys

sys.stdin = open("_포도주시식.txt")

wine = [0]*10000
N = int(input())
for i in range(N):
    wine[i] = int(input())
dp = [0] * 10000

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0]+wine[2], wine[1]+wine[2], dp[1])
for i in range(3,N):
    dp[i] = max(wine[i]+dp[i-2], wine[i]+wine[i-1]+dp[i-3], dp[i-1])

print(dp[N-1])


# data=map(int,open(0))
# n=next(data)
# a,b,c=0,0,0
# for i in data:
#     a,b,c=c+i,a+i,max(a,b,c)
# print(max(a,b,c))

# a,b,c=0,0,0
# for i in range(int(input())):
#     t=int(input())
#     a,b,c=max(a,b,c),a+t,b+t
# print(max(a,b,c))