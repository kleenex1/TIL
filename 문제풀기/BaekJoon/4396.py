N = int(input())

bomb = [list(input()) for _ in range(N)]
maps = [list(input()) for _ in range(N)]

ground = [['.'] * N for _ in range(N)]

dy = [0, 0, 1, 1, 1, -1, -1, -1]
dx = [1, -1, 0, 1, -1, 0, 1, -1]

지뢰_발견 = False

for i in range(N):
    for j in range(N):
        if maps[i][j] == 'x':
            지뢰 = 0        
            for d in range(8):
                r = i + dy[d]
                c = j + dx[d]
                if 0 <= r <= N - 1 and 0 <= c <= N - 1:
                    if bomb[r][c] == '*':
                        지뢰 += 1
            
            ground[i][j] = str(지뢰)
            if bomb[i][j] == '*':
                지뢰_발견 = True

if 지뢰_발견 == True:
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == '*':
                ground[i][j] = '*'

for row in ground:
    print(''.join(row))
                

            