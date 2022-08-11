
import sys
from collections import deque
sys.stdin = open("_DFS와BFS.txt", "r")



def dfs(V, discovered = []):
    discovered.append(V)
    print(V, end = ' ')

    for w in graph[V]:
        if w not in discovered:
            dfs(w, discovered)


def bfs(V):
    discovered = [V]
    queue = deque()
    queue.append(V)

    while queue:
        q = queue.popleft()
        print(q, end= ' ')

        for w in graph[q]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
for i in range(len(graph)):
    graph[i].sort()

dfs(V)
print()
bfs(V)