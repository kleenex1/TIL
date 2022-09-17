import sys

sys.stdin = open("_유니크.txt")

N = int(input())

games = [list(map(int,input().split())) for _ in range(N)]


games_set = []
for j in range(len(games[0])):
    game_set = []
    for i in range(N):
        game_set.append(games[i][j])
    games_set.append(game_set)

for i in range(N):
    for j in range(len(games[0])):
        if games_set[j].count(games[i][j]) > 1:
            games[i][j] = 0

for i in games:
    print(sum(i))