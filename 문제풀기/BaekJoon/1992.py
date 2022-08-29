import sys

sys.stdin = open("_쿼드트리.txt")

# n = int(input())

# tree = [list(map(int, input())) for _ in range(n)]
# result = []
# def quad(x,y,n):
#     color = tree[x][y]

#     for i in range(x, x+n):
#         for j in range(y, y+n):
#             if color != tree[i][j]:
#                 result.append("(")
#                 quad(x,y,n//2)
#                 quad(x,y+n//2, n//2)
#                 quad(x+n//2, y, n//2)
#                 quad(x+n//2, y+n//2, n//2)
#                 result.append(")")
#                 return
#     result.append(color)

# quad(0,0,n)
# print("".join(map(str, result)))


def decompose(n, y, x):
    # print(n, y, x)
    if n == 1:
        print(image[y][x], end="")
        return

    flag = True
    for i in range(y, y+n):
        if not flag:
            break
        for j in range(x, x+n):
            if image[i][j] != image[y][x]:
                flag = False
                break

    if flag:
        print(image[y][x], end="")
    else:
        decreased_n = n//2

        print("(", end="")
        decompose(decreased_n, y, x)
        decompose(decreased_n, y, x+decreased_n)
        decompose(decreased_n, y+decreased_n, x)
        decompose(decreased_n, y+decreased_n, x+decreased_n)
        print(")", end="")


N = int(input())
image = [list(input()) for _ in range(N)]
decompose(N, 0, 0)