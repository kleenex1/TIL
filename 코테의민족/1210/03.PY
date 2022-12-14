
# 리스트 -> insert 를 deque 쓰거나 appendleft를 쓰자
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


# 딕셔너리 !!
temp = {}
result = []
for idx, alpha in enumerate(s):
    if alpha not in temp:
        temp[alpha] = idx 
        result.append(-1)
    else:
        result.append(idx-temp[alpha])
        temp[alpha] = idx
print(result)

