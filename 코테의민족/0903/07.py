import sys
from collections import deque 
input = sys.stdin.readline
n, m = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(input()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,cnt):
    max_ = 0
    q = deque()
    q.append((x,y,cnt))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    while q:
        x,y,c = q.popleft()
        if max_ < c:
            max_ = c
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 'L' and visited[nx][ny] == 0:
                q.append((nx,ny,c+1))
                visited[nx][ny] = 1
    return max_

result = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == "L":
            result = max(result,bfs(i,j,0))

print(result)