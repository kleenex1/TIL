import sys

sys.stdin = open("_통역사.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x = list(input().split())
    ans = []
