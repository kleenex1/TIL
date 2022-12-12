import sys

sys.stdin = open("_연결요소.txt")

input = sys.stdin.readline
N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _  in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def dfs(num):
    stack = [num]
    while stack:
        x = stack.pop()
        if x not in visited:
            visited.append(x)
            for y in arr[x]:
                stack.append(y)
cnt = 0
visited=[]
for i in range(1, N+1):
    if i not in visited:
        dfs(i)
        cnt += 1
print(cnt)