# import sys

# sys.stdin = open("_민석이과제체크.txt")

# T = int(input())
# for tc in range(1,T+1):
#     N, K = map(int, input().split())
#     students = list(map(int, input().split()))
  
#     result = filter(lambda x: x not in students, list(range(1,N+1)))
#     print('#{} {}'.format(tc, ' '.join(list(map(str, result)))))
#     # unsubmit = []
#     # for i in range(1,N+1):
#     #     if i not in students:
#     #         unsubmit.append(str(i))
    
    print('#{} {}'.format(tc, ' '.join(unsubmit)))

n = int(input())
a = [int(input()) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(2)]
dp[1][1] = a[0]
if n >= 2:
    dp[0][2] = a[0] + a[1]
    dp[1][2] = a[1]
for i in range(3, n+1):
    dp[0][i] = dp[1][i-1] + a[i-1]
    dp[1][i] = max(dp[0][i-2], dp[1][i-2])
    
print(max(dp[0][n], dp[1][n]))