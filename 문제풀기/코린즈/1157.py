import sys

sys.stdin = open("_단어공부.txt")

S = input().upper()
words = list(set(S))

# 개수를 저장할 빈리스트
answer = []
for word in words:
    answer.append(S.count(word))

if answer.count(max(answer)) > 1:
    print("?")
else:
    print(words[(answer.index(max(answer)))])

