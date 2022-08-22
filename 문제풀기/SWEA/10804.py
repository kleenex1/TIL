import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
 
for test_case in range(1, T + 1):
     
    word = input()
     
    mirror = ''
    for char in word:
        if char == 'b':
            mirror += 'd'
        elif char == 'd':
            mirror += 'b'
        elif char == 'p':
            mirror += 'q'
        else:
            mirror += 'p'
 
    answer = mirror[::-1]
    print(f'#{test_case} {answer}')