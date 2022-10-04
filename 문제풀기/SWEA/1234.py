import sys

sys.stdin = open("_비밀번호.txt")

for tc in range(1, 11):
    N, password = input().split()
    stack = []
    for p in password:
        if stack and p == stack[-1]:
            stack.pop()
        else:
            stack.append(p)

    print('#{} {}'.format(tc, ''.join(stack)))