import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

fee = [INF]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
start, end = map(int, input().split())

q = [[0,start]]
fee[start] = 0

while q:
    f, n = heapq.heappop(q)

    if f > fee[n]:
        continue 
    else:
        for nn, nf in graph[n]:
            feee = nf + f
            
            if fee[nn] > feee:
                fee[nn] = feee 
                heapq.heappush(q, [feee,nn])
print(fee[end])

