T = int(input())

for test_case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A = W * P
    B = 0
    if W < R:
        B = Q 
        if A < B :
            print("#"+f'{test_case} {A}')
        else:
            print("#"+f'{test_case} {B}')
    else:
        B = Q + (W-R) * S
        if A < B :
            print("#"+f'{test_case} {A}')
        else:
            print("#"+f'{test_case} {B}')

# 다른 사람 코드..

T = int(input())
for i in range(1, i+1):
    P, Q, R, S, W = map(int, input().split())
    a = P * W
    b = Q if W <= R else Q + (W-R)*S
    result = a if a < b else b 
    
    print(f'#{i} {result}')