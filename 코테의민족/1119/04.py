def solution(number, limit, power):
    answer = 0
    for j in range(1,number+1):
        count = 0
        for i in range(1, int(j**(1/2)) + 1):
            if (j % i == 0):
                count += 1
                if ( (i**2) != j) :
                    count += 1 
        if count > limit:
            answer += power
        else:
            answer += count

    return answer
print(solution(10,3,2))