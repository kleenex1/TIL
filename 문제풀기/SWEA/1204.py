import sys

sys.stdin = open("1204_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    scores = map(int, input().split())
    list_ = [0] * 101

    for i in scores:
        list_[i] += 1
        
    m = max(list_)
    print("#{} {}".format(test_case, max([i for i, v in enumerate(list_) if v == m])))
    
    
