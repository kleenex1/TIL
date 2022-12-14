import heapq

INF = int(1e9)
city = int(input())
bus = int(input())
graph = [[] for _ in range(city+1)]

fee = [INF]*(city+1)
for _ in range(bus):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
start, end = map(int, input().split())

q = [[0,start]]
fee[start] = 0

while q:
    f, n = heapq.heappop(q)

    if f > fee[n]:
        # 노드, 간선이 많아질수있음 
        continue  
    else:
        for nn, nf in graph[n]:
            feee = nf + f
            
            if fee[nn] > feee:
                fee[nn] = feee 
                heapq.heappush(q, [feee,nn])
print(fee[end])



# def smallest():
#     min_value = INF
#     index = 0
#     for i in range(1, city+1):
#         if fee[i] < min_value and not visited[i]:
#             min_value = fee[i]
#             index = i
#     return index 

# def dijkstra(start):
#     fee[start] = 0
#     visited[start] = True 
#     for i in graph[start]:
#         if fee[i[0]] > i[1]:
#             fee[i[0]] = i[1]
#     for i in range(city-1):
#         now = smallest()
#         visited[now] = True 
#         for j in graph[now]:
#             cost = fee[now] + j[1]
#             if cost < fee[j[0]]:
#                 fee[j[0]] = cost 

# dijkstra(start)
# print(fee[end])