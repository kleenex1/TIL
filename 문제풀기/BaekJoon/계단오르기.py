import sys

sys.stdin = open("_계단오르기.txt")

N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [0] * N
if len(stairs) <= 2: 
	print(sum(stairs))
else:
	# 첫번째, 두번째 계단은 dp에 초기값으로 넣어준다.
	dp[0] = stairs[0] 
	dp[1] = stairs[0] + stairs[1]
	# 세번째 계단부터(dp[2]) 위에 점화식을 적용하여 구한다.
	# dp가 0번 인덱스가 1번째 계단이므로, 
	# range(2, N)으로 돌리면 N-1번 인덱스가 N번째 계단 
	for i in range(2, N):
		dp[i] = max(
		stairs[i] + stairs[i-1] + dp[i-3], 
		stairs[i] + dp[i-2]
		) 
	print(dp[-1])