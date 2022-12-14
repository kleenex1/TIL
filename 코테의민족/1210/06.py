import heapq 


INF = 1e9
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs():
    q = []
    heapq.heappush(q, (0,0,graph[0][0]))
    fee[0][0] = 0
    while q:
        x, y, cost = heapq.heappop(q)

        if x == T-1 and y == T-1:
            print(f'Problem {n}: {fee[x][y]}')
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < T and 0 <= ny < T :
                ncost = cost + graph[nx][ny]
                if fee[nx][ny] > ncost:
                    fee[nx][ny] = ncost 
                    heapq.heappush(q, (nx,ny,ncost))
                
    


n = 1
while True:
    T = int(input())
    if not T:
        break 
    
    graph = []
    fee = [[INF]*T for _ in range(T)]
    for _ in range(T):
        graph.append(list(map(int, input().split())))
            
    bfs()
    n += 1
