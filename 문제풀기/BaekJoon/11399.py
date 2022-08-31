import sys

sys.stdin = open("_ATM.txt")

N = int(input())
atm = list(map(int, input().split()))
sorted_atm = sorted(atm)
answer = 0

for i in range(len(sorted_atm)):
    answer += sorted_atm[i] * (len(sorted_atm)-i)

print(answer)