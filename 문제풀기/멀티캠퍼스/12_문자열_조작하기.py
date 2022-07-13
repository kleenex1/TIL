# 주어진 문자열 word가 주어질 때, 
# 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

list = []
def del_a(word):
    for i in word:
        list.append(i)
    while True:
        list.remove('a')
        if 'a' not in list:
            break
    result = ''.join(map(str, list))
    return result
        
a = del_a('appleafaadfaeft4ttfafaaa')   
print(a)