# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

1234
4321
# 문자열이면.. reverse / for문 거꾸로..
# number = 1234
# result = ''
# for num in number:
#     result = num + result  

# print(result)

def f(n):
    if n <=0: 
        return
    print(n%10, end='')
    f(n//10)

f(1234)