import sys

sys.stdin = open("_카드1.txt")

queue = list(range(1,int(input())+1))

while len(queue) > 1:
    print(queue.pop(0), end=" ")
    queue.append(queue.pop(0))

print(*queue)
