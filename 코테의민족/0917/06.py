import heapq 
import sys 
input = sys.stdin.readline
N = int(input())
q = []
for i in range(N):
    m = int(input())
    if m :
        heapq.heappush(q, (abs(m), m))
    elif m == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
