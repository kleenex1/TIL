N, M = map(int, input().split())

word = set([input() for _ in range(N)])
count = 0

for _ in range(M):
    word_ = input()
    if word_ in word:
        count += 1

print(count)


# 자료구조 문자열 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵


N, M = map(int, input().split())
arr = dict()
cnt = 0
for _ in range(N):
    s = input()
    arr[s] = True
for _ in range(M):
    inp = input()
    if inp in arr.keys():
        cnt += 1

print(cnt)