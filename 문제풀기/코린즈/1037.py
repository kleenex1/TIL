import sys

sys.stdin = open("_약수.txt")

N = int(input())
S = list(map(int, input().split()))
S.sort()
answer = S[0]*S[-1]

print(answer)