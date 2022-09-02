import sys

sys.stdin = open("_보물.txt")

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = 0
for i in range(N):
    s += min(A)*max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(s)