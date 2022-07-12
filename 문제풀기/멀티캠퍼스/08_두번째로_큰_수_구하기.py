# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100, 2000, 2000, 1999, 1999, 131]
max = numbers[0]

for num in numbers:
    if max <= num:
        max = num

while max in numbers:
    numbers.remove(max)

max2 = numbers[0]
for num in numbers:
    if max2 <= num:
        max2 = num
        
print(max2)