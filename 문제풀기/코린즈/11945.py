
import sys

sys.stdin = open("_뜨거운붕어빵.txt")

N, M = map(int, input().split())

fish = [input() for _ in range(N)]

for i in fish :
    print(i[::-1])