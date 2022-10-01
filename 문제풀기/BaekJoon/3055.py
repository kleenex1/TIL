import sys
from collections import deque

sys.stdin = open("_탈출.txt")

R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

player = deque()
water = deque()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

count = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            visited[i][j] = 1
            player.append((i,j))
        elif graph[i][j] == '*':
            visited[i][j] = 1
            water.append((i,j))
        elif graph[i][j] == 'X':
            visited[i][j] = 1
valid = False

while player:
    for _ in range(len(water)):
        x, y = water.popleft()
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.':
                    water.append((nx,ny))
                    graph[nx][ny] = '*'
                    visited[nx][ny] = 1
    
    count += 1

    for _ in range(len(player)):
        r, c = player.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < R and 0 <= nc < C:
                if graph[nr][nc] == '.':
                    if visited[nr][nc] == 0: 
                        player.append((nr,nc))
                        visited[nr][nc] = 1

                elif graph[nr][nc] == 'D':
                    print(count)
                    exit()

print("KAKTUS")
