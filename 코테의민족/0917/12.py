M, N = map(int, input().split())
graph = []
visited = [[0]*N for _ in range(M)]
for i in range(M):
    graph.append(list(map(int, input().split())))

dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,0,1,-1,0,1,-1]

def dfs(i,j):
    stack = [(i,j)]
    while stack:
        x, y = stack.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                stack.append((nx,ny))
                visited[nx][ny] = 1

count = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            if visited[i][j] == 0:
                dfs(i,j)
                count += 1
print(count)