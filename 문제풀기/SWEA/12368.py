import sys

sys.stdin = open("_24시간.txt")

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    
    
    if A + B > 24:
        print(f'#{tc} {A+B-24}')
    elif A + B == 24:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {A+B}')