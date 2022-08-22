import sys

sys.stdin = open("_외로운문자.txt")

T = int(input())
for tc in range(1, T+1):
    words = list(input())
    words.sort()
    stack = []

    for w in words:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)

    if stack:
        print(f'#{tc} {"".join(stack)}')
    else:
        print(f'#{tc} Good')

