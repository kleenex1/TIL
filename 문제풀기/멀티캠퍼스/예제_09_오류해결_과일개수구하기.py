# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# fruit_count = {fruit : 1} ?? 이부분.. 은 딕셔너리에 추가하는 것이 아니라 
# for문이 다 돌고나서 마지막 Salal berry : 1 만 출력하게 됨.
