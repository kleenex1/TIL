import sys

sys.stdin = open("_피보나치함수.txt")

# 저장해놓기 ?  어떻게

zero = [1, 0, 1]
one = [0, 1, 1]

# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)


def fibo(N):
    length = len(zero)
    if N >= length:
        for i in range(length, N+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("{} {}".format(zero[N], one[N]))

T = int(input())
for _ in range(T):
    N = int(input())
    fibo(N)