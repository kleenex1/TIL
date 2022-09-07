import sys

sys.stdin = open("_괄호.txt")

for i in range(int(input())):
    
    S = input()
    valid = True
    stack = []
    for i in S:
        if i == "(":
            stack.append(i)
        if i == ")" :
            if stack:
                stack.pop()
            else:
                valid = False
                break
    if valid and not stack:
        print("YES")
    else:
        print("NO")
