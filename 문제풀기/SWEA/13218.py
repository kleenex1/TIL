import sys

sys.stdin = open("_조별과제.txt")


T = int(input())

for test_case in range(1, T+1):
    nums = int(input())

    print('#{} {}'.format(test_case, nums//3))