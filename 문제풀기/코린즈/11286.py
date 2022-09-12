import sys
import heapq
sys.stdin = open("_절댓값힙.txt")

# 절댓값 힙은 x를 넣고(x != 0), 배열에서 절댓값이 가장 작은 값을 출력하고
# 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개 일때는, 가장 작은
# 수를 출력하고 그 값을 배열에서 제거한다.

input = sys.stdin.readline
N = int(input())

heap = []
for _ in range(N):
    A = int(input())
    if A:
        heapq.heappush(heap, (abs(A), A))
    else:
        if not heap:
            print(0)
        else : 
            print(heapq.heappop(heap)[1])
       