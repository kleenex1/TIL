import sys
sys.stdin = open("_유기농배추.txt")

T = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(a,b):
    stack = [(a,b)]
    graph[a][b] = 0
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                stack.append((nx,ny))
        



for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt += 1

    print(cnt)