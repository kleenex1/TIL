T = int(input())

bulk = []
for _ in range(T):
    bulk.append(list(map(int, input().split())))

rank = [1] * T
for i in range(T):
    for j in range(T):
        if (bulk[i][0] < bulk[j][0]) and (bulk[i][1] < bulk[j][1]):
            rank[i] = rank[i] + 1

print(*rank)

    