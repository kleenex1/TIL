import sys

sys.stdin = open("_자료구조는최고야.txt")
input = sys.stdin.readline

N, M = map(int, input().split())

valid = True
for _ in range(M):
    k = input()
    books = list(map(int, input().split()))
    for i in range(1, len(books)):
        if books[i - 1] < books[i]:
            valid = False
            break

if valid:
    print("Yes")
else:
    print("No")


import sys

sys.stdin = open("_단어뒤집기.txt")

T = int(input())
for _ in range(T):
    words = list(input().split())
    new = []
    for word in words:
        new.append(word[::-1])

    print(" ".join(new))

import sys

sys.stdin = open("_괄호짝짓기.txt")

for tc in range(1, 10 + 1):
    T = int(input())
    strings = list(input())
    stack = []
    valid = True
    for s in strings:
        if s in "{[(<":
            stack.append(s)
        elif s == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                valid = False
                break
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                valid = False
                break
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                valid = False
                break
        elif s == ">":
            if stack and stack[-1] == "<":
                stack.pop()
            else:
                valid = False
                break

    if valid:
        if not stack:
            print("#{} {}".format(tc, 1))
        else:
            print("#{} {}".format(tc, 0))
    else:
        print("#{} {}".format(tc, 0))
