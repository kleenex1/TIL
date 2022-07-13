# 주어진 문자열 word가 주어질 때, 
# 해당 단어를 역순으로 뒤집은 결과를 출력하시오.


list = []
def reverse_word(word):
    for i in word:
        list.append(i)
    list.reverse()
    result = ''.join(map(str, list))
    return result

a = reverse_word('apple')
print(a)