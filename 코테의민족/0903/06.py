from collections import deque

A,B,N,M = map(int, input().split())


dx = [-1,1,-A,A,-B,B,A,B]
def bfs(N,dist = [0]*100001):
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        for i in range(8):
            if i < 6:
                nx = x + dx[i]
                if 0 <= nx <= 100000 and visited[nx] == False:
                    q.append(nx)
                    visited[nx] = True
                    dist[nx] = dist[x] + 1
            else:
                nx = x * dx[i]
                if 0 <= nx <= 100000 and visited[nx] == False:
                    q.append(nx)
                    visited[nx] = True
                    dist[nx] = dist[x] + 1
    return dist[M]
visited = [False for _ in range(100001)]

print(bfs(N))