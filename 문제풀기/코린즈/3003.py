import sys

sys.stdin = open('_킹.txt')

chess = [1,1,2,2,2,8]

answer = list(map(int, input().split()))

for i, j in zip(chess, answer):
    print(i-j,end=' ')

