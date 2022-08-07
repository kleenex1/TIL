T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = ''
    for i in range(N):
        al, cnt = input().split()
        result += al * int(cnt)

    num = 0
    print(f'#{test_case}')
    for i in range(len(result)):
        print(result[i], end= '')
        num += 1
        if num == 10:
            num = 0
            print()
    print()