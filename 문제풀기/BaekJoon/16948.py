import sys
from collections import deque
sys.stdin = open("_데스나이트.txt")

N = int(input())
r1,c1,r2,c2 = map(int, input().split())

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

chess = [[-1]*N for _ in range(N)]
def bfs(r1,c1):
    queue = deque()
    queue.append((r1,c1))
    chess[r1][c1] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if chess[nx][ny] == -1: 
                    queue.append((nx,ny))
                    chess[nx][ny] = chess[x][y] + 1

bfs(r1,c1)
print(chess[r2][c2])    
    