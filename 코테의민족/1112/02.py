

food = [1,7,1,2]

def solution(food):
    answer = ''
    
    
    for i in range(len(food)) :
        answer += str(i) * (int(food[i])//2) 

 
    return answer + '0' + answer[::-1]

