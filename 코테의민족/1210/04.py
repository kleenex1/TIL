def solution(ingredient):
    burger = [1,2,3,1]
    answer = 0
    stack = []
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if stack[-4:] == burger:
            del stack[-4:]
            answer += 1
    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))