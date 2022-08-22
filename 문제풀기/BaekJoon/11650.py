import sys

sys.stdin = open("_좌표정렬.txt")

T = int(sys.stdin.readline())
plain = [tuple(map(int, sys.stdin.readline().split())) for _ in range(T)]
for i in sorted(plain, key = lambda x: (x[0],x[1])):
    print(*i)