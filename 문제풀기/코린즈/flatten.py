import sys 

sys.stdin = open("flatten.txt")

for tc in range(1,11):
    N = int(input())
    box = list(map(int, input().split()))
    for i in range(N):
        max_value = max(box)
        min_value = min(box)
        max_value_index = box.index(max_value)
        min_value_index = box.index(min_value)
        box[max_value_index] -= 1
        box[min_value_index] += 1
    answer = max(box) - min(box)
    print(f'#{tc} {answer}')