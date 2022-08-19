import sys

sys.stdin = open("_팔씨름.txt")

T = int(input())

for test_case in range(1, T+1):
    game = input()
    
    A = 15 - len(game)
    B = list(game)

    B.extend(["o"]*A)        
    
    if B.count("o") >= 8:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')
        