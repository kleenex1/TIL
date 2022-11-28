from collections import defaultdict

n = int(input())

ext = defaultdict(int)

for _ in range(n):
    a, files = input().split(".")
    ext[files] += 1

answer = sorted(ext.items())

for k,v in answer:
    print(k,v)