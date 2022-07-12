# 문자열 word의 길이를 출력하는 코드를 
# 각각 작성하시오 → *len() 함수 사용 금지
# Input  >> word = 'happy!'
# output >> 6

# 1)while문 
word = 'happy!'
n = 0

while True:
    try:
        word[n]
        n += 1
    except IndexError :
        break
print(n)

# 2)for문(문자열그대로) 
word = 'happy!'
n = 0
for letter in word:
    n += 1
print(n)

# 3)for문(index)
# 모르겠음



