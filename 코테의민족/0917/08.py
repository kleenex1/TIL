import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
count = 1
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(R):
    global count
    visited[R] = count
    for w in graph[R]:
        if visited[w] == 0:
            count += 1
            dfs(w)
    
    
    
for i in range(len(graph)):
    graph[i].sort()
dfs(R)

for i in range(1, N+1):
    print(visited[i])