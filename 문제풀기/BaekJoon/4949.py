
while 1:
    n = input()
    if n == '.':
        break

    stack = []
    flag = 1


    for i in n:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                break
        elif i ==']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 0
                break

            
    if flag and not stack:
        print("yes")
    else:
        print("no")    

# 자료구조 / 문자열 / 스택
