def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        answer.append(num_list[i:i+n])
    return answer


num_list = [1,2,3,4,5,6,7,8]
n = 2

print(solution(num_list,n))


n = 3
result = []
temp = []
# for idx, num in enumerate(num_list, 1:int시작하는숫자):
#     temp.append(num)
#     if not idx % n:
#         result.append(temp)
#         temp = []
    
#     print(idx, num)