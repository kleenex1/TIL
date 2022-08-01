import sys

sys.stdin = open("_파리퇴치.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    
    max_ = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_ = 0
            for k in range(M):
                for r in range(M):
                    sum_ += fly[i+k][j+r]
            
            if sum_ > max_:
                max_ = sum_
    print(f'#{test_case} {max_}')

