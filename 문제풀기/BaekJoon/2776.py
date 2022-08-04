# 자료구조 , 정렬, 이분탐색, 해시를 사용한 집합과 맵

T = int(input())

for _ in range(T):
    N = int(input())
    N_ = set(map(int, input().split()))
    M = int(input())
    M_ = list(map(int, input().split()))

    for num in M_:
        if num in N_:
            print(1)
        else:
            print(0)

# binary_search

def binary_search(s, e, nums1, num):
    while s <= e:
        mid = (s+e) // 2
        
        if nums1[mid] == num:
            return 1
        elif nums1[mid] < num:
            s = mid+1
        else:
            e = mid-1
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = list(map(int, input().split()))
    nums1.sort()
    m = int(input())
    nums2 = list(map(int, input().split()))
    for num in nums2:
        print(binary_search(0, n-1, nums1, num))