import sys

sys.stdin = open("04.txt")

T = int(input())

for tc in range(1, T+1):
    words = []
    max_length = 0
    for i in range(5):
        word = input()
        words.append(word)
        if len(word) > max_length:
            max_length = len(word)
    answer = ''
    for i in range(max_length):
        for j in range(5):
            if i < len(words[j]):
               answer += words[j][i]

    print(f'#{tc} {answer}') 
     