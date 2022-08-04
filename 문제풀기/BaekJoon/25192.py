T = int(input())


chat = dict()
count = 0
for _ in range(T):
    n = input()   
    if n == 'ENTER':
        for k, v in chat.items():
            if v == 1:
                count += 1
        chat = dict()
    else:
        if n not in chat:
            chat[n] = 1
    
for k, v in chat.items():
    if v == 1:
        count += 1
print(count)

# 자료구조 , 해시를 사용한 집합과 맵, 트리를 사용한 집합과맵