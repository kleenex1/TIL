import sys

sys.stdin = open("_그림.txt", "r")

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]


def dfs(i,j):
    cnt = 1
    stack = [(i,j)]
    if maps[i][j] == 1:
        maps[i][j] = 0
        while stack:
            x, y = stack.pop()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    stack.append((nx,ny))
                    cnt += 1
                            
    return cnt

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

count = 0
max_ = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 :
            max_ = max(max_, dfs(i,j))
            count +=1

print(count)
print(max_)