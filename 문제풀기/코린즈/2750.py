import sys
import heapq

sys.stdin = open("_수정렬하기.txt")

N = int(input())
heap = []
for _ in range(N):
    num = int(input())
    heapq.heappush(heap, num)

for _ in range(N):
    print(heapq.heappop(heap))