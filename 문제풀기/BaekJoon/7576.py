import sys
from collections import deque

sys.stdin = open('_토마토.txt')


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

queue = deque([])
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx,ny])
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

bfs()
valid = True
for i in graph:
    for j in i:
        if j == 0:
            valid = False
    answer = max(answer, max(i))
if valid:
    print(answer-1)
else:
    print(-1)