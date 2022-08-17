# 팩토리얼 N! = 1 * 2 * 3 * ... * N-2 * N-1 * N
# 0! = 1, 1! = 1

def factorial(N):
    result = 1
    if N > 0:
        result = N * factorial(N-1)
    return result

N = int(input())
print(factorial(N))