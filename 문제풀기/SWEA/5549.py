import sys
sys.stdin = open("_홀수일까짝수일까.txt")

for tc in range(int(input())):
    num = int(input())

    if num % 2 == 0 :
        print(f'#{tc+1} Even')
    else:
        print(f'#{tc+1} Odd')