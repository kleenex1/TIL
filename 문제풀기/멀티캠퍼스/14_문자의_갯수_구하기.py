# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지
# apple
# 1
# 테스트 케이스 
# banana # 3
# kiwi # 0
word = 'banana'
total = 0
for char in word :
    if char == 'a':
        total += 1

print(total)