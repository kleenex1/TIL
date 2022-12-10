from collections import deque 

N, K = map(int, input().split())
dist = [0] * (10**5 + 1)
data = [0] * (10**5 + 1)
def move(x):
    answer = []
    temp = x
    for _ in range(dist[x]+1):
        answer.append(temp)
        temp = data[temp]
    print(' '.join(map(str, answer[::-1])))


def bfs():
    q = deque()
    q.append(N)
    while q :
        x = q.popleft()
        if x == K:
            print(dist[x])
            move(x)
            return 
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 10**5 and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)
                data[nx] = x
bfs()