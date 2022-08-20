import sys

sys.stdin = open("_구구단1.txt")

T = int(input())

for tc in range(1, T+1):
    num = int(input())

    valid = False
    for i in range(1,10):
        for j in range(1,10):
            if i * j == num:
                valid = True

    if valid:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')
