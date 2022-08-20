import sys

sys.stdin = open("_Calkin.txt")

T = int(input())

for tc in range(1, T+1):
    tree = input()

    a = 1
    b = 1
    for i in tree:
        if i == "L":
            a, b = a, a+b
        if i == "R":
            a, b = a+b ,b
    print(f'#{tc} {a} {b}')