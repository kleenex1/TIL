import sys

sys.stdin = open("_공과잡초.txt")

T = int(input())

for test_case in range(1, T + 1):
    ball = input()
    cnt = 0
    cnt += ball.count("()")
    cnt += ball.count("(|")
    cnt += ball.count("|)")

    print(f'#{test_case} {cnt}')