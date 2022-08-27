# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

word = "HappyHacking"

count = 0

for char in word:
    if char in 'aeiou' :
        count += 1

print(count)

# if char == 'a' or "e" or "i" or "o" or "u": 라고 하면 or 뒤에 부분이 true?로되기떄문에
# 글자 전체를 세는 오류를 범하게됨. in으로 바꿔줌.
