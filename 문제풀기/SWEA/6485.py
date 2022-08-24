import sys

sys.stdin = open("_삼성시.txt")

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    
    bus = dict()
    for i in range(1,5001):
        bus[i] = 0

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus[i] += 1

    P = int(input())
    answer = []

    for i in range(P):
        answer.append(bus[int(input())])
    
    print(f'{tc}', *answer)

     