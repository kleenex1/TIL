import sys
import math
sys.stdin = open("_제곱펠린드롬.txt")

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())

    cnt = 0
    for i in range(A,B+1):
        C = math.sqrt(i)
        if C == int(C):
            i = str(i)
            C = str(int(C))
            if i == i[::-1] and C == C[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')