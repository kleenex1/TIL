import sys

sys.stdin = open("_성지키기.txt")

N, M = map(int, input().split())

castle = [list(input()) for _ in range(N)]

original = 0
original_90 = 0

for row in range(N):
    if "X" not in castle[row]:
        original += 1

castle2 = []
temp = []
for row in range(M):
    for col in range(N):
        temp.append(castle[col][row])
    castle2.append(temp)
    temp = []

for row in range(len(castle2)):
    if "X" not in castle2[row]:
        original_90 += 1

print(max(original,original_90))