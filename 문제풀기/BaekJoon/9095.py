import sys

sys.stdin = open("_123더하기.txt")

# def plus(num):
#     if num == 1:
#         return 1
#     if num == 2:
#         return 2
#     if num == 3:
#         return 4
#     else:
#         return plus(num-1) + plus(num-2) + plus(num-3)


# T = int(input())
# for _ in range(T):
#     num = int(input())
#     print(plus(num))



#dp 로 풀기

T = int(input())
for _ in range(T):
    num = int(input())
    dp = [1,2,4]
    for i in range(3, num):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    
    print(dp[num-1])
    
    
