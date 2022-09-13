import sys

sys.stdin = open("_암호.txt")

r = int(input())
words = input()
c = int(len(words)/r)

answer = []
n = 0
for i in range(0,len(words),r):
    if n % 2 == 0:
        answer.append(list(words[i:(i+r)]))
    if n % 2 == 1:
        answer.append(list(words[(i+r-1):i-1:-1]))
    n += 1

result = ''
for i in range(r):
    for j in range(c):
        result += answer[j][i]

print(result)