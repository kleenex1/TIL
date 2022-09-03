import sys
from collections import deque
sys.stdin = open("_팰린드롬수.txt")


def palin(num):
    queue = deque()

    for char in num:
        queue.append(char)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

while True:
    num = input()
    if num == '0':
        break
    if palin(num):
        print("yes")
    else:
        print("no")
