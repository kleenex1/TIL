location = [[0 for i in range(19)] for j in range(19)]

for i in range(19):
    location[i] = list(map(int, input().split()))

n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    for j in range(19):
        if location[j][y - 1] == 0:
            location[j][y - 1] = 1
        else:
            location[j][y - 1] = 0

        if location[x - 1][j] == 0:
            location[x - 1][j] = 1
        else:
            location[x - 1][j] = 0

for all in location:
    print(*all)