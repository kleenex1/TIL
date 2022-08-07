import sys

sys.stdin = open("_1959.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
        
    list_ = []
    if N > M :
        for i in range(N-M+1):
            result = []
            for k in range(len(B)):
                result.append(B[k]*A[k+i])
            list_.append(sum(result))
    else:
        for i in range(M-N+1):
            result = []
            for k in range(len(A)):
                result.append(B[k+i]*A[k])
            list_.append(sum(result))

    print(f'#{test_case} {max(list_)}')