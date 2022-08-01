T = int(input())

store = list(map(int, input().split()))

count = 0

for i in range(T):
    if count%3 == store[i] :
        count += 1

print(count)
