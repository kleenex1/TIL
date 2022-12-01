from collections import deque
import sys
def bfs():
    global s 
    q = deque()
    visited[0][0] = 1
    q.append((0,0))
    while q:
        x, y = q.popleft()
        if maps[x][y] == 2:
            s = n-1-x + m-1-y + visited[x][y]-1
        if x == n-1 and y == m-1:
            return min(visited[x][y]-1, s)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return s 

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m, limit = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
s = sys.maxsize
result = bfs()
print("Fail" if result>limit else result)