import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    answer = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for r in range(M):
                for c in range(M):
                    kill += flies[i+r][j+c]
            answer.append(kill)

    print('#{} {}'.format(tc,max(answer)))