from collections import deque 

N, K = map(int, input().split())

maps = []
virus = []
for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(N):
        if maps[i][j] != 0:
            virus.append((maps[i][j],i,j))

S, X, Y = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(s, x, y):
    q = deque(virus)
    cnt = 0
    while q:
        if cnt == s:
            break 
        for _ in range(len(q)):
            a, b, c = q.popleft()
            for i in range(4):
                nx = b + dx[i]
                ny = c + dy[i]
                if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 0:
                    maps[nx][ny] = maps[b][c]
                    q.append((maps[nx][ny],nx,ny))
        cnt += 1 
    return maps[x-1][y-1]

virus.sort()
print(bfs(S,X,Y))