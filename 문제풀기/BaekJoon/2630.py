import sys

sys.stdin = open("_색종이만들기.txt")


result = []
def paper(x,y,n):
    p = color[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if p != color[i][j]:
                paper(x, y, n//2)
                paper(x, y+n//2, n//2)
                paper(x+n//2, y, n//2)
                paper(x+n//2,y+n//2, n//2)
                return
    if p == 0:
        result.append(0)
    else:
        result.append(1)

n = int(input())
color = [list(map(int, input().split())) for _ in range(n)]
paper(0,0,n)
print(result.count(0))
print(result.count(1))
