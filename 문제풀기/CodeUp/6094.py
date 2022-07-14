n = int(input())
a = input().split()

b = list(map(int, a))
print(min(b))

n = int(input())
a = list(map(int, input().split()))
ans = a[0]

for i in range(n):
    if a[i] < ans:
        ans = a[i]

print(ans)