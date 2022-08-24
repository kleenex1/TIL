import sys

sys.stdin = open("_다솔이월급.txt")

for tc in range(int(input())):
    N = int(input())
    ans = 0
    for _ in range(N):
        p, x = map(float, input().split())
        ans += p*x

    print(f'#{tc+1} {ans}')