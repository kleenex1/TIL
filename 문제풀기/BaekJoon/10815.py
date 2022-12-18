
N = int(input())
S = set(map(int, input().split()))
M = int(input())
P = list(map(int, input().split()))

count = {}
for i in P:
    if i in S:
        count[i] = 1
    else:
        count[i] = 0
    

for k, v in count.items():
    print(v, end=' ')