import sys
from datetime import datetime
sys.stdin = open('_태혁이.txt')
T = int(input())

for tc in range(1, T+1):
    D,H,M = map(int, input().split())
    d = datetime(2011,11,11,11,11)
    s = datetime(2011,11,D,H,M)
    if d-s>0:
        print(f'#{tc} {d-s}')
    else:
        print(f'#{tc} {-1}')

    