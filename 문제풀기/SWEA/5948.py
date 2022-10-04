import sys
from itertools import combinations
sys.stdin = open("_새샘이.txt")

T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    combi = list(combinations(nums,3))    
    list_ = []
    for i in combi:
        list_.append(sum(i))
    set_ = list(set(list_))
    set_.sort(reverse=True)
    print('#{} {}'.format(tc, set_[4]))

    
    
    