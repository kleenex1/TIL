array = []

for i in range(10):
    array.append(list(map(int, input().split())))

x, y = 1, 1

while True:
    if array[x][y] == 0:
        array[x][y] = 9
    elif array[x][y] == 2:
        array[x][y] = 9
        break
    if (array[x][y+1]==1 and array[x+1][y] == 1) or (x==9 and y==9):
        break

    if array[x][y+1] != 1:
        y += 1
    elif array[x+1][y] != 1:
        x += 1


for ant in array :
    print(*ant)

# 계속 답만 보네.. 백준부터는 답 보지말고 해야지 !!
