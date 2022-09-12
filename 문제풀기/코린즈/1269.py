import sys

sys.stdin = open("_대칭차집합.txt")

# 공집합이 아닌 두집합 AB가 있는데 두집합의 대칭 차집합의 원소의 개수를 출력하는?
# A-B와 B-A의 합집합.

A, B = input().split()

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

print(len((A_set - B_set) | (B_set - A_set)))