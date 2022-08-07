import sys

sys.stdin = open("_1961.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(str, input().split())) for _ in range(N)]
    answer = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            answer[i][j] = matrix[N-j-1][i]
    
    answer1 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            answer1[i][j] = answer[N-j-1][i]

    answer2 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            answer2[i][j] = answer1[N-j-1][i]

    print(f'#{test_case}')
    for i in range(N):
        print(''.join(answer[i]), ''.join(answer1[i]), ''.join(answer2[i]))
