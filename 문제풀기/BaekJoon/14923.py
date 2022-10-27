import sys
from collections import deque
sys.stdin = open('_미로탈출.txt')

N, M  = list(map(int, input().split()))
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
miro = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque()
    q.append((Hx-1,Hy-1,0))
    visited[Hx-1][Hy-1][0] = 0
    
    while q:
        x,y,crash = q.popleft()
        if x == Ex-1 and y == Ey-1:
            return visited[x][y][crash]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if crash == 0 and miro[nx][ny] == 1 and visited[nx][ny][crash] == -1:
                    visited[nx][ny][crash+1] = visited[x][y][crash] + 1
                    q.append((nx,ny,1))
                elif miro[nx][ny] == 0 and visited[nx][ny][crash] == -1:
                    visited[nx][ny][crash] = visited[x][y][crash] + 1
                    q.append((nx,ny,crash))

    return -1

print(bfs())
print(visited)

# 입력값, 3차원 visisted 이해!!
