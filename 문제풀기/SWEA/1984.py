import sys

sys.stdin = open("_중간평균값.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))

    answer = ((sum(numbers)-max(numbers)-min(numbers)) / 8)
    print('#{} {:.0f}'.format(test_case, answer))

    