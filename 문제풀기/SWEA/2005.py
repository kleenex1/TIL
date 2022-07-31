T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    paskal = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                paskal[i][j] = 1
            else:
                paskal[i][j] = paskal[i-1][j] + paskal[i-1][j-1]
    print(f'#{test_case}')
    for lst in paskal:
        result = [x for x in lst if x]
        print(*result)