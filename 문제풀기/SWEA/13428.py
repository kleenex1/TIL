import sys

sys.stdin = open("_숫자조작.txt")

T = int(input())
for test_case in range(1, T+1):
    nums = list(input())
    
    min_ = int(''.join(nums))
    max_ = int(''.join(nums))
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if i == 0 and nums[j] == "0":
                continue 
            nums[i], nums[j] = nums[j], nums[i]
            min_ = min(min_, int(''.join(nums)))
            max_ = max(max_, int(''.join(nums)))
            nums[i], nums[j] = nums[j], nums[i]
    
    print(f'#{test_case} {min_} {max_}')