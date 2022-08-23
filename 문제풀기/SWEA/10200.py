import sys

sys.stdin = open("_구독자전쟁.txt")

T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())

    max_ = 0
    min_ = 0
    min_ = min(A,B)
    max_ = A+B-N if A+B > N else 0
    print(f'#{tc} {min_} {max_}')        