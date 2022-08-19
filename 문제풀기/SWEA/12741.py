import sys

sys.stdin = open("_두전구.txt")

T = int(input())

ans = ''
for test_case in range(1, T+1):
    A, B, C, D = map(int, input().split())
    answer = len(set(range(A,B)) & (set(range(C,D))))
    ans += f'#{test_case} {answer}\n'

print(ans, end='')


