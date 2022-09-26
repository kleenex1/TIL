import sys

sys.stdin = open("_면적구하기.txt")

graph = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2 = map(int, input().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[i][j] = 1

answer = 0
for i in graph:
    answer += sum(i)
print(answer)