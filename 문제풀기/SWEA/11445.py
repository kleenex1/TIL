import sys

sys.stdin = open("_무한사전.txt")

T = int(input())

for tc in range(1, T+1):
    P = input().rstrip()
    Q = input().rstrip()

    if P + "a" != Q:
        print(f'#{tc} Y')
    else:
        print(f'#{tc} N')

    