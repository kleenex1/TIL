import sys

sys.stdin = open("_평범한숫자.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    
    cnt = 0
    for q in range(1, n-1):
        if lst[q-1] < lst[q] < lst[q+1] or lst[q+1] < lst[q] < lst[q-1]:
            cnt += 1

    print(f'#{tc} {cnt}')