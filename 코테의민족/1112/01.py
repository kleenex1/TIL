import sys

sys.stdin = open('01.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    if N % 2 == 0:
        print('#{} Alice'.format(tc))
    else:
        print('#{} Bob'.format(tc))