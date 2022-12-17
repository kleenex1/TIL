from collections import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    q = deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

bfs()
print(graph[N-1][M-1])