import sys

sys.stdin = open("_격자판칠하기.txt")

T = int(input())


for test_case in range(1, T+1):
    N, M = map(int, input().split())
    paint = [input() for _ in range(N)]
    
    s = set()
    b = set()
    q = set("?")
    for i in range(N):
        for j in range(M):
            if (i+j) % 2 == 0:
                s.add(paint[i][j])
            else:
                b.add(paint[i][j])
    

    if len(s - q) == 2 or len(b - q) == 2:
        print(f'#{test_case} impossible')
    elif (s - q) & (b - q):
        print(f'#{test_case} impossible')
    else:
        print(f'#{test_case} possible')