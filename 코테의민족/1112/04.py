import sys
from collections import deque

a, b, c, d = map(int, sys.stdin.readline().split())


visit = {}

def bfs():
    queue = deque()
    queue.append((0, 0))
    visit[(0, 0)] = 1

    if c == 0 and d == 0:
        return 0
    
    while queue:

        x, y = queue.popleft()

        # a 가득채우기
        if not visit.get((a, y)):
            queue.append((a, y))
            visit[(a, y)] = visit[(x, y)] + 1

        # b 가득채우기
        if not visit.get((x, b)):
            queue.append((x, b))
            visit[(x, b)] = visit[(x, y)] + 1


        # a 비우기
        if not visit.get((0, y)):
            queue.append((0, y))
            visit[(0, y)] = visit[(x, y)] + 1


        # b 비우기
        if not visit.get((x, 0)):
            queue.append((x, 0))
            visit[(x, 0)] = visit[(x, y)] + 1


        # a -> b 옮기기
        if x <= b - y:
            if not visit.get((0, x + y)):
                queue.append((0, x + y))
                visit[(0, x + y)] = visit[(x, y)] + 1

        else:
            if not visit.get((x + y - b, b)):
                queue.append((x + y - b, b))
                visit[(x + y - b, b)] = visit[(x, y)] + 1


        # b -> a 옮기기
        if y<= a - x:
            if not visit.get((x + y, 0)):
                queue.append((x + y, 0))
                visit[(x + y, 0)] = visit[(x, y)] + 1

        else:
            if not visit.get((a, x + y - a)):
                queue.append((a, x + y - a))
                visit[(a, x + y - a)] = visit[(x, y)] + 1

        if visit.get((c, d)):
            if visit[(x, y)]>0:
                return (visit[(x, y)])

    return -1


print(bfs())