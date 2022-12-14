T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = list(input().split())
    answer = 0
    for i in nums:
        answer += int(i[:len(i)-1])**int(i[-1])
    print(answer)