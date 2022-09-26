import sys

sys.stdin = open("_암호생성기.txt")

for tc in range(1, 11):
    T = int(input())
    password = list(map(int, input().split()))

    while password[-1] != 0:
        for i in range(1, 5+1):
            if password[0] - i > 0:
                password.append(password[0] - i)
            if password[0] - i <= 0:
                password.append(0)
                break
            del password[0]
    del password[0]

    print('#{} {}'.format(tc, ' '.join(map(str, password))))