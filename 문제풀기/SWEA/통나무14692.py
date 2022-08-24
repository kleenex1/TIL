import sys
sys.stdin = open("_통나무.txt")

T = int(input())
for tc in range(1, T+1):
    tree = int(input())
    # 두 조각으로 나눈다. 자연수로 잘려야 한다.
    # A 2 -> B 1 : A 승
    # A 3을 나누면 2, 1 -> B 2 -> A 1 : Bob 승 
    #      A    10
    #        5          5
    #     3   2      3   2
    #   2  1 1 1    2 1 1  1
    #  1 1          1 1 
    # 
    