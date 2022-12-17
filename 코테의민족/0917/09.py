import sys 
from collections import deque
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
count = 1
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(R):
    global count
    q = deque()
    q.append(R)
    visited[R] = 1
    while q:
        i = q.popleft()
        for w in graph[i]:
            if visited[w] == 0:
                count += 1
                visited[w] = count
                q.append(w)
    
    
    
for i in range(len(graph)):
    graph[i].sort()
bfs(R)

for i in range(1, N+1):
    print(visited[i])