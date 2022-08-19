import sys

sys.stdin = open("_일요일.txt")

lst = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

T = int(input())
for test_case in range(1, T+1):
    day = input()

    if day == "SUN":
        print(f'#{test_case} 7')
    else:
        print(f'#{test_case} {6 - lst.index(day)}')
 