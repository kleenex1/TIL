n = int(input())

enter, out = dict(), []
answer = 0
for i in range(n):
    car = input()
    enter[car] = i

for _ in range(n):
    car = input()
    out.append(car)

for i in range(n-1):
    for j in range(i+1, n):
        if enter[out[i]] > enter[out[j]]:
            answer += 1
            break
print(answer)