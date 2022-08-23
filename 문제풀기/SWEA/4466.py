import sys

sys.stdin = open("_최대성적.txt")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    scores.sort(reverse = True)
    answer = 0
    for i in range(K):
        answer += scores[i]
    print(f'#{tc} {answer}')            