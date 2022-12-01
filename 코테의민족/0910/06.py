T = int(input())


dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(i,j):
    stack = [(i,j)]
    graph[i][j] = 2
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 2
                stack.append((nx,ny))


for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*N for _ in range(M)]
    for j in range(K):
        X, Y = map(int, input().split())
        graph[X][Y] = 1 
        
    cnt = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt += 1

    print(cnt)        