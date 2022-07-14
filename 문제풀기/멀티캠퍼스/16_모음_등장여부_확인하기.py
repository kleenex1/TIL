# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

# apple
# 2

# aeiou # 5
# zxcvb # 0

모음 = ['a', 'e', 'i', 'o', 'u']
word = 'aeiou'
count = 0
for char in word:
    if char in 모음:
        count += 1
print(count)