import sys

sys.stdin = open("_공.txt")

N = int(input())

ball = [1,2,3]
for _ in range(N):
    N, M = map(int, input().split())
    Np = ball.index(N)
    Mp = ball.index(M)
    
    ball[Np], ball[Mp] = ball[Mp], ball[Np]

print(ball[0])