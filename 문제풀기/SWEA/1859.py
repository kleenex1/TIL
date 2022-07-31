import sys

sys.stdin = open("_백만장자.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    price = list(map(int, input().split()))
    
    goga = price[-1]
    earn = 0

    for i in range(n-2, -1, -1):
        if price[i] >= goga:
            goga = price[i]
        else:
            earn += goga - price[i]
    
    print('#{} {}'.format(test_case, earn))