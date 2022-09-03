import sys
sys.stdin = open("_30.txt")

N = list(map(int, input()))

B = sum(N)
new = sorted(N, reverse=True)

if B%3 == 0:
    C = new[-1]
    if C == 0:
        answer = ''.join(map(str, new))
        print(int(answer))
    else:
        print(-1)

else:
    print(-1)