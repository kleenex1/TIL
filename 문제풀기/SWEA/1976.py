T = int(input())

for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    minute = b + d
    hour = a + c
    if minute > 59:
        minute %= 60 
        hour += 1 
    if hour % 12 == 0:
        hour = 12
    else:
        hour = hour % 12
   
    print(f'#{test_case} {hour} {minute}')