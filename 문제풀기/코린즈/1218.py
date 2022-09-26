import sys

sys.stdin = open("_괄호짝짓기.txt")

for tc in range(1,11):
    N = int(input())
    strings = input()

    stack = []
    valid = True
    
    for i in strings:
        if i in "([{<" :
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                valid = False
                break
            
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                valid = False
                break
            
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                valid = False
                break
            
        elif i == '>':
            if stack and stack[-1] == '<':
                stack.pop()
            else:
                valid = False
                break
    if not stack:
        if valid:
            print(f'#{tc} 1')
        else:
            print(f'#{tc} 0')
    else:
        print(f'#{tc} 0')