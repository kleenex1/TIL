import sys

sys.stdin = open("_반반.txt")

T = int(input())

for tc in range(1, T+1):
    alpha = input()

    s = dict()
    for i in alpha:
        if i not in s:
            s[i] = 1
        else:
            s[i] += 1
    if len(s) != 2:
        print(f'#{tc} No') 
    else:
        print(f'#{tc} Yes') 