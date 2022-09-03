import sys
import heapq

sys.stdin = open("_카드정렬하기.txt")

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    answer = 0
    while len(cards) > 1:
        temp1 = heapq.heappop(cards)
        temp2 = heapq.heappop(cards)
        answer += temp1 + temp2
        heapq.heappush(cards, temp1+temp2)
    
    print(answer)