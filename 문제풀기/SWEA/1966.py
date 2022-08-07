import heapq
import sys

sys.stdin = open("_1966.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    heap = []
    numbers = list(map(int, input().split()))
    for num in numbers:
        heapq.heappush(heap, num)
    
    print(f'#{test_case}', end = ' ') 
    for _ in range(N):
        print(heapq.heappop(heap), end = ' ')
    print()