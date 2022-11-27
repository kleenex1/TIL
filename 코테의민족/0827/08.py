import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs1(i,j):
    global count
    q = deque()
    q.append([i,j])
    v[i][j] = True
    maps[i][j] = cnt 

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1 and not v[nx][ny]:
                v[nx][ny] = True
                maps[nx][ny] = cnt 
                q.append([nx,ny])

def bfs2(num):
    global answer 
    dist = [[-1]*n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if maps[i][j] == num:
                q.append([i,j])
                dist[i][j] = 0 

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if maps[nx][ny] > 0 and maps[nx][ny] != num:
                answer = min(answer, dist[x][y])
                return
            if maps[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx,ny])

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
v = [[False]*n for _ in range(n)]
cnt = 1
answer = sys.maxsize 

for i in range(n):
    for j in range(n):
        if not v[i][j] and maps[i][j] == 1:
            bfs1(i, j)
            cnt += 1

for i in range(1, cnt):
    bfs2(i)

print(answer)