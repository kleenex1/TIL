# 문자열 word가 주어질 때, 
# Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

# banana
# b 1
# a 3
# n 2

word = 'banana'
count = {}
for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for key, value in count.items():
    print(key, value)