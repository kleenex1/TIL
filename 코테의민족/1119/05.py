import sys
from collections import deque
sys.stdin = open("05.txt")

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(n)]

v = [0, deque(), deque()]
cnt1, cnt2, cnt3 = 1, 1, 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(n):
    for j in range(m):
        if town[i][j] >= 1:
            v[town[i][j]].append((i,j))

while v[1] or v[2]:
    tmp1, tmp2 = set(), set()

    while v[1]:
        x, y = v[1].popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and town[nx][ny] == 0:
                tmp1.add((nx,ny))
    
    while v[2]:
        x, y = v[2].popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and town[nx][ny] == 0:
                tmp2.add((nx,ny))
    
    tmp3 = tmp1 & tmp2
    for x, y in tmp3:
        town[x][y] = 3
        cnt3 += 1

    for x, y in tmp1 - tmp3:
        town[x][y] = 1
        v[1].append((x,y))
        cnt1 += 1

    for x, y in tmp2 - tmp3:
        town[x][y] = 2
        v[2].append((x,y))
        cnt2 += 1

print(cnt1, cnt2, cnt3)