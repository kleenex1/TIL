import sys

sys.stdin = open("_1979.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for i in range(N):
        count_ = []
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            else:
                count_.append(cnt)
                cnt = 0
        count_.append(cnt)
        answer += count_.count(K)

    for i in range(N):
        count_ = []
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            else:
                count_.append(cnt)
                cnt = 0
        count_.append(cnt)
        answer += count_.count(K)
            
    print(f'#{test_case} {answer}')


