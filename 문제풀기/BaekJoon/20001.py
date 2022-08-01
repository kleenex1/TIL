list_ = []

while 1:
    Q = input()
    if Q == '문제':
        list_.append('문제')
    elif Q == '고무오리':
        if not list_:
            list_.append('문제')
            list_.append('문제')
        else:
            list_.pop()
    elif Q == '고무오리 디버깅 끝':
        break
if not list_ :
    print("고무오리야 사랑해")
else:
    print("힝구")

