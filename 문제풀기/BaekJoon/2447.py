# 별 찍기 - 10

# N이 3의 거듭제곱이라고 할때 크기 N의 패턴은 N*N 정사각형 모양이다
# 크기 3의 패턴은 가운데에 공백이 있고 가운데를 제외한 모든 칸에 별이 하나씩 있다
# N이 3보다 클 경우 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)*(N/3) 정사각형을 크기 N/3의
# 패턴으로 둘러싼 형태이다.  N은 3의 거듭제곱이다. 

# 종료조건 ? : 
# 문제의 정의 : (N/3)*(N/3)에는 별이 없다. 

def star(N):
    if N == 1:
        return ['*']
    
    stars = star(N//3)
    L = []

    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s+' '*(N//3)+s)
    for s in stars:
        L.append(s*3)
    return L

n = int(input())
print('\n'.join(star(n)))