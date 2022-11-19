# 매개변수를 하나만 받고 dfs로 풀수는 없나?

def solution(number):
    answer = []
    for i in range(0, len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer.append([number[i],number[j],number[k]])
                                   
    return len(answer)