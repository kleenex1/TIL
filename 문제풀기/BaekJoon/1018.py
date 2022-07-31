N, M = map(int, input().split())

chess = []
for _ in range(N):
    chess.append(input())

count = []
for i in range(N-8+1):
    for j in range(M-8+1):
        start_W = 0
        start_B = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if chess[a][b] != 'W':
                        start_W += 1
                    if chess[a][b] != 'B':
                        start_B += 1
                else:
                    if chess[a][b] != 'B':
                        start_W += 1
                    if chess[a][b] != 'W':
                        start_B += 1
        count.append(min(start_W, start_B))

print(min(count))
