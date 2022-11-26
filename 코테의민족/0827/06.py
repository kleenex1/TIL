M, N, K = map(int, input().split())

maps = [[0]* N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(y1,y2):
        for y in range(x1,x2):
            maps[x][y] = 1


dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(i, j):
    stack = [(i,j)]
    maps[i][j] = 1
    count = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and maps[nx][ny] == 0:
                stack.append((nx,ny))
                maps[nx][ny] = 1
                count += 1   
    return count

answer = []
for i in range(M):
    for j in range(N):
        if maps[i][j] == 0:
            answer.append(dfs(i,j))

print(len(answer))
answer.sort()
print(*answer)