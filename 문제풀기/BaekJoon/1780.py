import sys

sys.stdin = open("_종이의개수.txt")

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = []
def tree(x,y,n):
    p = paper[x][y]
    
    for i in range(x,x+n):
        for j in range(y, y+n):
            if p != paper[i][j]:
                for r in range(3):
                    for c in range(3):
                        tree(x+r*n//3,y+c*n//3,n//3)
                return
    if p == 0:
        result.append(0)
    elif p == -1:
        result.append(-1)
    else:
        result.append(1)

tree(0,0,n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))