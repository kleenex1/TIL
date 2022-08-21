import sys

sys.stdin = open("_몬스터사냥.txt")

T = int(input())

for tc in range(1, T+1):
    D, L, N = map(int, input().split())
    
    answer = 0
    for i in range(N):
        answer += D*1+D*i*(L/100)

    print(f'#{tc} {round(answer)}')