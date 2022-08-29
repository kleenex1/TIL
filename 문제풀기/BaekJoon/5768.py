import sys

sys.stdin = open("_divide.txt")


while True:
    M, N = map(int, input().split())
    if (M, N) == (0, 0):
        break

    count = 0
    k = 0
    for i in range(M,N):
        cnt = 0
        for j in range(1,i+1):
            if i%j == 0:
                cnt += 1
        if count <= cnt:
            count = cnt
            k = i
        
    print(k, count)
            
