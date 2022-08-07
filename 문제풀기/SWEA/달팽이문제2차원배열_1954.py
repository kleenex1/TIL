
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 1 # 달팽이 배열에 넣는 수 초기화
    x, y = 0, -1 # 달팽이 인덱스 초기화 
    k = 0 # 방향 설정

    while cnt <= N*N:
        r, c = x+dx[k], y+dy[k]

        if 0 <= r <= N - 1 and 0 <= c <= N - 1 and snail[r][c] == 0:
            snail[r][c] = cnt
            cnt += 1
            x, y = r, c 
        else:
            k = (k+1) % 4

    
    print(f'#{test_case}')
    for row in snail:
        print(*row)
