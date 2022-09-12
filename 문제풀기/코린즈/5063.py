import sys

sys.stdin = open("_TGN.txt")

N = int(input())
for _ in range(N):
    r, e, c = map(int, input().split())
    if e-c > r:
        print("advertise")
    if e-c < r:
        print("do not advertise")
    if e-c == r:
        print("does not matter")