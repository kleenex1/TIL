import sys

sys.stdin = open("_KMP.txt")

S = list(input().split('-'))

for i in S:
    print(i[0],end="")