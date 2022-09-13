import sys

sys.stdin = open("_행렬덧셈.txt")

N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

B = []
for _ in range(N):
    B.append(list(map(int, input().split())))

answer = []
for a, b in zip(A,B):
    for j, k in zip(a, b):
        answer.append(j+k)

for i in range(0, len(answer),3):
    print(*answer[i:i+3])
