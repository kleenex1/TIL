import sys

sys.stdin = open("_유니크.txt")

N = int(input())

games = [list(map(int,input().split())) for _ in range(N)]


# 행/열 바꿔주기 
total_set = [[0]*N for _ in range(3)]

for i in range(3):
    for j in range(N):
        total_set[i][j] = games[j][i]
print(total_set)
# 원래 그래프에서 값 바꿔주기
for i in range(N):
    for j in range(3):
        if total_set[j].count(games[i][j]) > 1:
            games[i][j] = 0

for i in games:
    print(sum(i))