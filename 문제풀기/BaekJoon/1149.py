import sys

sys.stdin = open("_RGB.txt")

# 2차원으로 받고 3개씩 끊어서 
# 26이면 60 57 중에 작은거, 60일때 13, 99 중에 작은거, 57일때 13, 89 중에 작은거

N = int(input())
house = []
for i in range(N):
    house.append(list(map(int, input().split())))

#빨/초/파
#파/빨/초
#빨/초/파

# 0, 1, 2
for i in range(1,N):
    # 첫번째가 빨강이면 
    house[i][0] = min(house[i-1][1],house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i-1][0],house[i-1][2]) + house[i][1]
    house[i][2] = min(house[i-1][0],house[i-1][1]) + house[i][2]

print(min(house[N-1]))