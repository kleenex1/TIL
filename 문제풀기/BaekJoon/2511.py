A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
    print(10, 10)
    print("D")
else:
    a = b = 0
    for i in range(10):
        if A[i] > B[i]:
            a += 3
            winner = 'A'  # 체크포인트!!
        elif A[i] == B[i]:
            a += 1
            b += 1
        else:
            b += 3
            winner = 'B' # 체크포인트!!
    print(a, b)
    if a == b:
        print(winner)
    else:
        print('A' if a>b else 'B')

