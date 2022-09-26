import sys

sys.stdin = open("_어디에단어가.txt")

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for i in range(N):
        word = []
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            else:
                word.append(cnt)
                cnt = 0
        word.append(cnt)
        answer += word.count(K)
    for i in range(N):
        word = []
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            else:
                word.append(cnt)
                cnt = 0
        word.append(cnt)
        answer += word.count(K)

    print('#{} {}'.format(tc,answer))