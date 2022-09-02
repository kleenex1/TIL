import sys

sys.stdin = open("_전자레인지.txt")

T = int(input())
microwave = [300,60,10]

count = []
for i in microwave:
    count.append(T//i)
    T %= i

if not T:
    print(*count)
else:
    print(-1)   
