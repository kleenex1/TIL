T = int(input())

for test_case in range(1, T+1):

    word = input()
    if word[::-1] == word:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')

# 한줄 혹은 함수로 표현하는 방법 생각해보기