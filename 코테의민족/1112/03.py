import sys

sys.stdin = open('03.txt')

T = int(input())

for tc in range(1, T+1):
    s, t = input().split()
    len_s, len_t = len(s), len(t)
    if s * len_t == t * len_s:
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')