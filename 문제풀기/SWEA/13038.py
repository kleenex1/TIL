import sys

sys.stdin = open("_교환학생.txt")

'''
7개의 정수 a1,a2,a3,,,a7로 표현된다 ai = 0 or ai = 1
수업이열리면 1 아니면 0으로 표현
어떠한 요일에도 열리지 않는 경우는 없다. 하나의 요일에는 열린다.
수업을 n번 들어야 된다. 
'''
T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    week = list(input().split())

    result = 1e9
    for i in range(7):
        if week[i] == "1":
            idx = i
            cnt = 0
            m = n
            while m:
                if week[idx] == "1":
                    m -= 1
                cnt += 1
                idx = (idx + 1) % 7    
            if result > cnt:
                result = cnt

    print(f'#{test_case} {result}')