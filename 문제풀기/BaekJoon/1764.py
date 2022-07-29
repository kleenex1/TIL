# 딕셔너리
N, M = map(int, input().split())
    
dict_ = dict()
for _ in range(N):
    p = input()
    dict_[p] = "듣도못한"

list_=[]
for _ in range(M):
    p = input()
    if p in dict_:
        list_.append(p)

print(len(list_))
for p in sorted(list_):
    print(p)


# set
N, M = map(int, input().split())

d = set()
b = set()

for _ in range(N):
    d.add(input())
for _ in range(M):
    b.add(input())

result = sorted(d&b)

print(len(result))
print(*result, sep='\n')

