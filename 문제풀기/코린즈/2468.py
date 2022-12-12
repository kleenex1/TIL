from collections import deque
import sys 

sys.stdin = open("안전영역.txt")

N = int(input())
graph = []
m = 0
l = 0
for _ in range(N):
    i = list(map(int, input().split()))
    graph.append(i)
    m = max(i)
    l = len(i)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(i,j,num):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > num and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))

result = 0
for num in range(m):
    cnt = 0
    visited = [[0]*l for _ in range(N)]
    for i in range(N):
        for j in range(l):
            if graph[i][j] > num and visited[i][j] ==0 :
                bfs(i,j,num)
                cnt += 1

    if result <= cnt :
        result = cnt

print(result)