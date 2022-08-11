import sys
sys.stdin = open("_섬의개수.txt", "r")




dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [0, 1, -1, 1, -1, 0, 1, -1]

def dfs(i,j):
    stack = [(i,j)]
    visited[i][j] = True
    while stack:
        i, j = stack.pop()
        for d in range(8):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    maps = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]

    island = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == False:
                dfs(i,j)
                island += 1

    print(island)