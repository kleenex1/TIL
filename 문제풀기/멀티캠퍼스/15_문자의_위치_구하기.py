# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

# banana
# 1
# apple # 0
# kiwi # -1
word = 'banana'
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        break
else:
    print(-1)

# ?? 이건 어떤 풀이??    
is_a = False
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        is_a = True
        break
if not is_a:
    print(-1)


# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

# HappyHacking
# 1 6

word = 'banana'
n = 0
for i in word:
    if i == 'a':
        print(n, end=' ')
    n += 1