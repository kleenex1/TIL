import sys

sys.stdin = open("_정사각형판정.txt")


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i,j):
    stack = [(i,j)]
    visited[i][j] = 1
    cnt = 1
    minX, minY, maxX, maxY = i, j, i, j
    while stack:
        x, y = stack.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if maps[nx][ny] == '#':
                    cnt += 1
                    visited[nx][ny] = 1
                    minX = min(minX, nx)
                    minY = min(minY, ny)
                    maxX = max(maxX, nx)
                    maxY = max(maxY, ny)
                    stack.append((nx,ny))
                    
    sx = maxX - minX + 1
    sy = maxY - minY + 1
    result = ''                
    if sx == sy:
        if sx * sx == cnt:
            result = "yes"
        else:
            result = "no"
    else:
        result = "no"
    return result


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maps = [list(input()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    # count_ = 0
    # for i in maps:
    #     count_ += i.count("#")

    valid = False
    for i in range(N):
        for j in range(N):
            if maps[i][j] == '#' and visited[i][j] == 0:
                if valid:
                    answer = "no"
                    break
                valid = True
                answer = dfs(i,j)

    # if count_ == 1:
    #     print(f'#{test_case} yes')
    # else:    
    print(f'#{test_case} {answer}')

# from collections import deque
 
# t = int(input())
 
# dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
 
# def bfs(a ,b):
#     visited[a][b] = 1
#     que = deque()
#     que.append([a, b])
 
#     # 가운데 값이 비어있는지 확인용
#     countSharp = 1
#     # 정사각형인지 확인하기 위한 좌표 입력
#     minX, minY, maxX, maxY = a, b, a, b
#     while que:
#         x, y = que.popleft()
 
#         for dx, dy in dxy:
#             nx = dx + x
#             ny = dy + y
#             if 0 <= nx < n and 0 <= ny < n:
#                 if visited[nx][ny] == 0 and square[nx][ny] == '#':
#                     visited[nx][ny] = 1
#                     countSharp += 1
#                     minX = min(minX, nx)
#                     minY = min(minY, ny)
#                     maxX = max(maxX, nx)
#                     maxY = max(maxY, ny)
 
#                     que.append([nx, ny])
#     print(countSharp)
#     # 사각형의 밑변
#     sx = maxX - minX + 1
#     # 사각형의 높이
#     sy = maxY - minY + 1
     
#     result = "-1"
#     if sx == sy:
#         if sx ** 2 == countSharp:
#             result = "yes"
#         else:
#             result = "no"
#     else:
#             result = "no"
     
#     return result
 
# for case in range(1, t + 1):
#     n = int(input())
 
#     square = []
#     for _ in range(n):
#         square.append(list(input().strip()))
     
#     flag = False
#     visited = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if square[i][j] == '#' and visited[i][j] == 0:                
#                 if flag:
#                     result = "no"
#                     break
#                 flag = True
#                 result = bfs(i, j)
     
#     print(f"#{case} {result}")
            