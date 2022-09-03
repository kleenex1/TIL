import sys

sys.stdin = open("_그대로출력하기2.txt")

while True:
    try:
        N = input()
        print(N)
    except EOFError:
        break