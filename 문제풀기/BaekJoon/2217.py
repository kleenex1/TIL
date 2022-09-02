import sys

sys.stdin = open("_로프.txt")

N = int(input())
rope = [int(input()) for _ in range(N)]

rope.sort(reverse=True)
for i in range(N):
    rope[i] = rope[i] * (i+1)

print(max(rope))