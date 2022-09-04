import sys

sys.stdin = open("_오르막길.txt")

N = int(input())
nums = list(map(int, input().split()))

height = 0
height_list = []

for i in range(1, N):
    if nums[i] > nums[i-1]:
        height += nums[i] - nums[i-1]
        if i == N-1:
            height_list.append(height)

    else:
        height_list.append(height)
        height = 0
print(max(height_list))