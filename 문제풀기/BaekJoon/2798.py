N, M = map(int, input().split())

black = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if black[i] + black[j] + black[k] > M:
                continue
            else:
                result = max(result, black[i] + black[j] + black[k])
print(result)