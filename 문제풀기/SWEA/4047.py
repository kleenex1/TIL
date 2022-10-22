import sys

sys.stdin = open('_영준이의카드.txt')

T = int(input())

for tc in range(1, T+1):
    cards = input()
    S = [0]*13
    D = [0]*13
    H = [0]*13
    C = [0]*13
    
    for i in range(0,len(cards),3):
        alpha = cards[i]
        num = int(cards[i+1:i+3]) - 1
        if alpha == 'S':
            S[num] += 1
            
        if alpha == 'D':
            D[num] += 1
            
        if alpha == 'H':
            H[num] += 1
            
        if alpha == 'C':
            C[num] += 1
            
    
    answer = [S.count(0), D.count(0), H.count(0), C.count(0)]
    result = ' '.join(map(str,answer))
    if 2 in S or 2 in D or 2 in H or 2 in C:
        print(f'#{tc} ERROR')
    else:
        print('#{} {}'.format(tc, result))

