N,M,K = map(int, input().split())

maps = [[0]*M for _ in range(N)]
for _ in range(K):
    a, b = input().split()
    a = int(a)
    b = int(b)
    maps[a-1][b-1] = 1

visited = [[0]*M for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(i,j,cnt):
    cnt = 1
    stack = [(i,j)]
    visited[i][j] = 1
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and maps[nx][ny] == 1 :
                visited[nx][ny] = 1
                stack.append((nx,ny))
                cnt += 1
    return cnt     
                            
result = 0  

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            result = max(result, dfs(i,j,1))

print(result)