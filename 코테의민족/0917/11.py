import sys 
from collections import deque 

def location():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                bomb.append((i,j))

def full():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 'O':
                graph[i][j] = 'O'

def bombs():
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while bomb:
        a, b = bomb.popleft()
        graph[a][b] = "."
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0 <= na < r and 0 <= nb < c:
                if graph[na][nb] == "O":
                    graph[na][nb] = "."

r, c, n = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]
n -= 1
while n:
    bomb = deque()
    location()
    full()
    n -= 1 
    if n == 0:
        break 
    bombs()
    n -= 1

for i in graph:
    print("".join(i))