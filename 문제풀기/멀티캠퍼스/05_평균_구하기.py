# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지
# numbers = [3, 10, 20] >> 11
numbers = [3, 10, 20]
count = 0
sum = 0
for i in numbers:
    count += 1
    sum += i
print(int(sum/count))

