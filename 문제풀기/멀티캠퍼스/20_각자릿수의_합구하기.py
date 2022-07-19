# 정수 number가 주어질때, 각 자릿수의 합을 구해서 출력

# number = 123456789
# num_str = str(number)

# list = []
# list_int = []
# for num in range(len(num_str)):
#     list.append((num_str[num]))
# for each in list:
#     list_int.append(int(each))

# print(sum(list_int))

list = []
def f(n):
    if n <=0: 
        return
    list.append(n%10)
    f(n//10)    
    return list
a = f(12345)
print(sum(a))


## 강사님 코드

number = 123
result = 0
while number:
    result += number%10
    number //= 10

print(result)

number = 123
result = 0
while number:
    number, remainder = divmod(number, 10)
    result += remainder
print(result)