T = int(input())

won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]


for test_case in range(1, T + 1):
    money = int(input())
    numbers = []
    for i in range(len(won)):
        if numbers.append(money // won[i]) != 0:
            money -= (money // won[i])*won[i]
        else:
            numbers.append(money // won[i])

    print(f'#{test_case}')
    print(*numbers)