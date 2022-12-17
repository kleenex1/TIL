from collections import deque 


def dfs(V):
    visited = []
    stack = [V]

    while stack:
        w = stack.pop()
        if w not in visited:
            print(w, end=' ')
        visited.append(w)
        temp = []
        for i in graph[w]:
            if i not in visited:
                temp.append(i)
        temp.sort(reverse=True)
        stack += temp        

def bfs(V):
    visited = [V]
    q = deque()
    q.append(V)
    
    while q:
        i = q.popleft()
        print(i, end=' ')

        for w in graph[i]:
            if w not in visited:
                q.append(w)
                visited.append(w)
    


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

dfs(V)
print()
bfs(V)
