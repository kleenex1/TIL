import sys  
from collections import deque
sys.stdin = open("적록색약.txt")

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(input()))



dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                visited[nx][ny] = 1
                q.append((nx,ny))

# 아닌경우
normal = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j)
            normal += 1

# 적록색약
for i in range(N):
    for j in range(N):
        if graph[i][j] == "R":
            graph[i][j] = "G"



visited = [[0]*N for _ in range(N)]
abnor = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j)
            abnor += 1

print(normal, abnor)