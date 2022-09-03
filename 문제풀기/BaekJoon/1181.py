import sys

sys.stdin = open("_단어정렬.txt")

N = int(input())
words = [input() for _ in range(N)]

answer = sorted(words, key = lambda x: (len(x),x))
# 한번만 출력
for i in range(1, len(answer)):
    if answer[i-1] != answer[i]:
        print(answer[i-1])
print(answer[-1])


