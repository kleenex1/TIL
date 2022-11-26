import sys

sys.stdin = open("05.txt")

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(i,j):
    stack = [(i,j)]
    visited[i][j] = 1
    while stack:
        x, y = stack.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 16 and 0 <= ny < 16 and maps[nx][ny] == '0':
                if visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    stack.append((nx,ny))
            elif 0 <= nx < 16 and 0 <= ny < 16 and maps[nx][ny] == '3':
                if visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    stack.append((nx,ny))
                return 1
    return 0 

for _ in range(1, 11):
    tc = input()
    maps = []
    visited = [[-1] * 16 for _ in range(16)]
    for i in range(16):
        maps.append(list(input()))

    for i in range(16):
        for j in range(16):
            if maps[i][j] == '2':
                print(f'#{tc} {dfs(i,j)}')
                