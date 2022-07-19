# 45분 일찍 알람 설정하기
# 케이스분류

H, M = map(int, input().split())

early = M - 45 

if early < 0 and H == 0:
    print(f'23 {M + 15}')
elif early < 0 and H > 0:
    print(f'{H-1} {M + 15}')
elif early >= 0 and H >=0:
    print(f'{H} {early}')