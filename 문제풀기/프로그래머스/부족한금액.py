

def solution(price, money, count):
    total = 0

    for i in range(1,int(count)+1):
        total += price*i 

    if money - total > 0:
        return 0  
    else:
        return total - money


print(solution(3,20,4))