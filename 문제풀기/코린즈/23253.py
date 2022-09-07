import sys

sys.stdin = open("_자료구조는최고야.txt")
input = sys.stdin.readline
N, M = map(int, input().split())

valid = True
for _ in range(M):
    input()
    books = list(map(int, input().split()))

    for i in range(1,len(books)):
        if books[i-1] < books[i]:
            valid = False

if valid:
    print("Yes")
else:
    print("No")