h, w = map(int, input().split())
shape = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())

for _ in range(n):
    l, d, x, y = map(int, input().split())
    x, y = x-1, y-1

    if d == 0:
        for i in range(l):
            shape[x][y+i] = 1
    else:
        for i in range(l):
            shape[x+i][y] = 1

for b in shape:
    print(*b)