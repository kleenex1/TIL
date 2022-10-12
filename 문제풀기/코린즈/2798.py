import sys
from itertools import combinations

sys.stdin = open("_블랙잭.txt")

N, M = map(int, input().split())

black = list(map(int, input().split()))

# answer = 0
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             if black[i] + black[j] + black[k] >= M:
#                 continue
#             else:
#                 result = max(answer, black[i] + black[j] + black[k])
# print(answer)

answer = 0

for card in combinations(black,3):
    print(type(card))
    total = sum(card)
    if answer < total <= M:
        answer = total
print(answer)