import sys

sys.stdin = open("_배부른마라토너.txt")

input = sys.stdin.readline

N = int(input())
m = dict()


for i in range(N):
    s = input()
    if s in m:
        m[s] += 1
    else:
        m[s] = 1

for i in range(N-1):
    s = input()
    if s in m:
        m[s] -= 1

for i in m:
    if m[i]:
        print(i)
        break