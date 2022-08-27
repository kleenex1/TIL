#1부터 n까지의 합을 구하여 출력하는 코드

# 1) while
n = 0
result = 0
while n < 10:
    n += 1
    result += n 
print(result)


# 2) for문
n = 10
total = 0
for num in range(n+1):
    total += num

print(total)