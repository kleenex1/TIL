import sys

sys.stdin = open("_암호.txt")

r = int(input())
words = input()
c = len(words)/r

answer = ''

for i in range(len(words)):
    if i % 2 == 0:
        answer += words[i*r:(i+1)*r]
    else:
        answer += words

print(answer)