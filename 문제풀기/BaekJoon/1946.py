import sys

sys.stdin = open("_신입사원.txt")
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    test = [list(map(int, input().split())) for _ in range(N)]

    test_sorted = sorted(test, key= lambda x: x[0])
    answer = 1
    compare = test_sorted[0][1]
    for i in range(1,N):
        if test_sorted[i][1] < compare:
            compare = test_sorted[i][1]
            answer += 1

    print(answer)
    