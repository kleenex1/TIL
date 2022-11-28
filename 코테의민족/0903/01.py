from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)

    for i in report:
        a,b = i.split()
        user[a].add(b)
        cnt[b] += 1

    for i in id_list:
        result = 0 
        for j in user[i]:
            if cnt[j] >= k:
                result += 1
        answer.append(result)

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list,report,k))

# https://dongdongfather.tistory.com/69

