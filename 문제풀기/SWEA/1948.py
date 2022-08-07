from datetime import date

T = int(input())
for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    A = date(1, a, b)
    B = date(1, c, d)

    print('#{} {}'.format(test_case, (B-A).days + 1))