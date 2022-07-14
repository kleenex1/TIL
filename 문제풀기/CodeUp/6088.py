
# 시작값 = a
# 등차 = d
# 몇번째인지 나타내는 정수 = n

a, d, n = map(int, input().split())
print(a + (d*(n-1)))