import sys 
sys.stdin = open("사과빨리먹기.txt")


graph = []
for i in range(5):
    graph.append(list(map(int, input().split()))) 

r, c = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0]*5 for _ in range(5)]

def dfs(r,c,cnt):
    stack = [(r,c)]
    cnt = 0
    if cnt == 3:
        return 

    while stack:
        x, y = stack.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and graph[nx][ny] == 1:
                stack.append((nx,ny))
                dfs(r,c,cnt+1)
                

