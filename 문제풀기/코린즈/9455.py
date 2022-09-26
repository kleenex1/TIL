import sys

sys.stdin = open("_박스.txt")

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    box_new = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            box_new[i][j] = box[j][i]
    
    answer = 0
    for new in box_new:
        for i in range(len(new)):
            if new[i] == 1:
                cnt = new[i+1:].count(0)
                answer += cnt

    print(answer)