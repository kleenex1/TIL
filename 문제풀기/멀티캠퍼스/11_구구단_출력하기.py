# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

def 구구단():
    for i in range(2, 9 + 1):
        print(f'{i}단')
        for j in range(1, 9 + 1):
            print(f'{i} X {j} = {i*j}')
    

구구단()

