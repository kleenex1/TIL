from re import S
import sys

sys.stdin = open("_주유소.txt")

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
price = B[0]
for i in range(N-1):
    if price > B[i]:
        price = B[i]    
    answer += price*A[i]

print(answer)