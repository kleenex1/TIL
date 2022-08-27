# 1부터 n까지의 곱을 구하여 출력하는 코드를
# 1) while 문 2) for 문으로 각각 작성하시오.

# 1) While 문

# 1) while
n = 0
result = 1
while n < 5:
    n += 1
    result *= n 
print(result)


# 2) for문
n = 5
total = 1
for num in range(1, n+1):
    total *= num
print(total)