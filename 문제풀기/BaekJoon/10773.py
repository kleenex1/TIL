T = int(input())

numbers = []
for _ in range(T):
    number = int(input())
    if number == 0:
        numbers.pop()
    else:
        numbers.append(number)
        
print(sum(numbers))