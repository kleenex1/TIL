memo = list(map(str, input().split('-')))

answer = ''
for i in range(len(memo)):
    answer += memo[i][0]

print(answer)