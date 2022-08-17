# 0 부터 
# n-1 + n-2 = n
# N = 1 -> 0 N = 2 -> 1
def f(N):
    if N <=1:
        return N
    return f(N-1) + f(N-2)

print(f(10))