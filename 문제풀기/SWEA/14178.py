import sys

sys.stdin = open('_1차원정원.txt')

T = int(input())

for test_case in range(1, T+1):
    N, D = map(int, input().split())
    
    if N % (2*D + 1) == 0:
        print(f'#{test_case} {N // (2*D+1)}')
    if N % (2*D + 1) != 0:
        print(f'#{test_case} {N // (2*D+1) + 1}')