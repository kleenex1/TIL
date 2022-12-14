T = int(input())
for tc in range(1,T+1):
    N, D = map(int, input().split())
    answer = 0
    if not N % (D*2+1):
        answer = N // (D*2+1)
    else:
        answer = N // (D*2+1) + 1
        
    print(f'#{tc} {answer}')
