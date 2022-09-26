import sys

sys.stdin = open('_누울자리를찾아라.txt')

N = int(input())

rooms = [list(input()) for _ in range(N)]


row = []
for i in range(N):
    count = []
    cnt = 0
    for j in range(N):
        if rooms[i][j] != 'X':
            cnt += 1
        else:
            count.append(cnt)
            cnt = 0
    count.append(cnt)
    row.append([k for k in count if k >= 2])

rooms_col = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        rooms_col[i][j] = rooms[j][i]

col = []
for i in range(N):
    count = []
    cnt = 0
    for j in range(N):
        if rooms_col[i][j] != 'X':
            cnt += 1
        else:
            count.append(cnt)
            cnt = 0
    count.append(cnt)
    col.append([k for k in count if k >= 2])

row_answer = 0
for i in row:
    row_answer += int(len(i))

col_answer = 0
for j in col:
    col_answer += int(len(j))

print(row_answer, col_answer)