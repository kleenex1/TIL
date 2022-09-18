import sys
# 시간초과 나는 풀이
sys.stdin = open("_2차원배열의합.txt")
input = sys.stdin.readline
N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

# for _ in range(int(input())):
#     i,j,x,y = map(int, input().split())
#     result = 0
#     for k in range(i-1,x):
#         for c in range(j-1,y):
#             result += array[k][c]
#     print(result)

# 시간초과를 해결해보자.
# 부분합, 누적합 개념 필수.

sum_array = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum_array[i][j] = array[i-1][j-1] + sum_array[i-1][j] + sum_array[i][j-1] - sum_array[i-1][j-1]

def acc(S,i,j,x,y):
    return S[x][y] - S[x][j-1] - S[i-1][y] + S[i-1][j-1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(acc(sum_array,i,j,x,y))