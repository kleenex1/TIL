import sys
import math
sys.stdin = open("_다트게임.txt")

point = [400,1600,3600,6400,10000,14400,19600,25600,32400,40000]


T = int(input())
for tc in range(1, T+1):
    total = 0
    for i in range(int(input())):
        x, y = map(int, input().split())
        b = math.pow(x,2) + math.pow(y,2)
        for p in point:
            if b > 40000:
                continue
            elif b <= p:
                total += 10-point.index(p)
                break  
    print(f'#{tc} {total}')

from math import ceil,sqrt
answers = []
for t in range(1, int(input())+1):
    ans = 0
    for i in range( int(input()) ):
        x,y = map(int,input().split())
        r = ceil(sqrt(x*x + y*y)/20) if (x,y) != (0,0) else 1
        if r <= 11:
            ans += 11-r
    answers.append(f'#{t} {ans}')
print(*answers,sep="\n")