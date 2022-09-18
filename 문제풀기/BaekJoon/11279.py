import sys
import heapq

sys.stdin = open("_최대힙.txt")

N = int(input())
array = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if array:
            print(-heapq.heappop(array))
        else:
            print(0)
    else:
        heapq.heappush(array, -x)
    