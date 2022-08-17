import sys

sys.stdin = open("_통계학.txt")


N = sys.stdin.readline()
s = [int(sys.stdin.readline()) for _ in range(int(N))]

# 산술평균
print('{}'.format(round(sum(s)/int(N))))

# 중앙값
s.sort()
print(s[(int(N)-1)//2])


# 최빈값
cnt = dict()
for i in s:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

max_ = max(cnt.values())
second = []

for k, v in cnt.items():
    if v == max_:
        second.append(k)

second.sort(reverse = True)

if len(second) >= 2:
    print(second[second.index(min(second))-1])
else:
    print(second[0])


# 범위
print(max(s) - min(s))