import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    incomes = list(map(int, input().split()))
    avg = sum(incomes) // num

    cnt = 0
    for income in incomes:
        if income <= avg:
            cnt += 1

    print(f'#{tc} {cnt}')