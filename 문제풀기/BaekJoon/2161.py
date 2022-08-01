T = int(input())

queue = list(range(1, T + 1))

while len(queue) > 1:
    print(queue.pop(0), end =" ")
    queue.append(queue.pop(0))

print(queue[0])