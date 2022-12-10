def solution(s):
    answer = []
    result = []
    for w in s:
        if w not in result:
            answer.append(-1)
            result.insert(0,w)
        elif w in result:
            answer.append(result.index(w)+1)
            result.insert(0,w)
    return answer

s = "banana"
print(solution(s))