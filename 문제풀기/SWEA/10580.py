import sys

sys.stdin = open("_전봇대.txt")

T = int(input())

for tc in range(1, T+1):
    nums = int(input())

    
    case = [tuple(map(int, input().split())) for _ in range(nums)]
    cnt = 0
    for i in range(len(case)-1):
        for j in range(i+1, len(case)):
            if (case[i][0] > case[j][0] and case[i][1] < case[j][1]) or \
                (case[i][0] < case[j][0] and case[i][1] > case[j][1]):
                cnt += 1
    print(f'#{tc} {cnt}')