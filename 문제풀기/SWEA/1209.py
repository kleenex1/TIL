import sys
sys.stdin = open("_sum.txt")

for tc in range(1, 11):
    T = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    
    max_row = 0
    max_col = 0
    for i in range(100):
        sum = 0
        sum1 = 0
        for j in range(100):
            sum += graph[i][j]
            sum1 += graph[j][i]
        if max_row < sum:
            max_row = sum
        if max_col < sum1:
            max_col = sum1
    
    max_cross = 0
    for i in range(100):
        sum2 = 0
        sum3 = 0
        sum2 += graph[i][i]
        sum3 += graph[i][99-i]
    if max_cross < max(sum2,sum3):
        max_cross = max(sum2,sum3)

    print("#{} {}".format(tc, max(max_row,max_col,max_cross)))