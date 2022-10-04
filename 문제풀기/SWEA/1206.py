import sys

sys.stdin = open("_View.txt")

for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    
    view = 0
    for i in range(0, N-3):
        if max(buildings[i:i+5]) == buildings[i+2]:
            view += buildings[i+2] - sorted(buildings[i:i+5])[-2]
    
    print('#{} {}'.format(tc,view))