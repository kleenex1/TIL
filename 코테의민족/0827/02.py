def solution(answers):
    answer = []
    fir = [1,2,3,4,5] * 2000
    sec = [2,1,2,3,2,4,2,5] * 1250
    thi = [3,3,1,1,2,2,4,4,5,5] * 1000
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == fir[i]:
            cnt1 += 1
        if answers[i] == sec[i]:
            cnt2 += 1
        if answers[i] == thi[i]:
            cnt3 += 1

    temp = [0,cnt1,cnt2,cnt3]
    max_v = max(temp)
    for i in range(len(temp)):
        if max_v == temp[i]:
            answer.append(i)

    return answer

answers = [1,3,2,4,2]
print(solution(answers))