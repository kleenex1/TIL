import sys

sys.stdin = open("_숫자가같은배수.txt")

T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    valid = False
    for i in range(2,10):
        if set(list(str(i*num))) == set(list(str(num))):
            valid = True
    
    if valid :
        print(f'#{test_case} possible')
    else:
        print(f'#{test_case} impossible')
