# 1) 숫자를 리스트에 담는다 . [0,0,0,0,0,0,0,0,0,0]
# 2) 0의 값이 없을때까지 while을 돌린다 ? 
# 3) 숫자가 다 채워지면 그때 카운트를 센다.

T = int(input())

for test_case in range(1, T + 1):
    sheep = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    num = int(input())
    count = 1
    while 0 in sheep:
        for i in str(num*count):
            sheep[int(i)] += 1
        count += 1
        

    print(f"#{test_case} {num*(count-1)}")

