import sys

sys.stdin = open("_균형잡힌세상.txt")

while True:
    S = input()
    if S == '.':
        break
    stack = []
    valid = 1
    for char in S:
        if char == "(" or char == "[":
            stack.append(char)
        if char == ")":
            if stack and stack[-1] == "(":
                stack.pop(-1)
            else:
                valid = 0
                break
        if char == "]":
            if stack and stack[-1] == "[":
                stack.pop(-1)
            else:
                valid = 0
                break
    if valid and not stack:
        print("yes")
    else:
        print("no")
    
 