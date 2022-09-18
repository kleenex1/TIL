import sys

sys.stdin = open('_단지번호붙이기.txt')

N = int(input())

apartment = [list(input()) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    global cnt 

    if x < 0 or x >= N or y < 0 or y >= N:
        return
    
    if apartment[x][y] == "1":
        cnt += 1
        apartment[x][y] = "0"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

result = []
cnt = 0
for i in range(N):
    for j in range(N):
        if apartment[i][j] == "1":
            dfs(i, j)
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for k in result:
    print(k)


# BFS
from collections import deque
def bfs(graph,a,b):
    queue = deque()
    queue.append([a,b])
    graph[a][b] = "0"
    count = 1
    
    while queue:
        x, y = queue.popleft()
        graph[x][y] = "0"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue

            if graph[nx][ny] == "1":
                graph[nx][ny] = "0"
                queue.append([nx,ny])
                count += 1
    return count

result = []
for i in range(N):
    for j in range(N):
        if apartment[i][j] == "1":
            count = bfs(apartment,i,j)
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i)