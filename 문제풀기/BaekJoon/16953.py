import sys
from collections import deque

sys.stdin = open("_AB.txt")

A, B = map(int, input().split())

queue = deque()
queue.append((A,1))
while queue:
    x, cnt = queue.popleft()
    if x > B:
        continue
    if x == B:
        print(cnt)
        break
    queue.append((int(str(x)+"1"),cnt+1))
    queue.append((x*2,cnt+1))
  
else:
    print(-1)