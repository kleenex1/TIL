# result = []

# def dfs(index, path):
#     result.append(path)
    
#     for i in range(index, len(words)):
#         dfs(i+1, path+[words[i]])

# dfs(0, [])
# print(dfs) 


babbling = ["aya", "yee", "u", "maa"]

def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]

    cnt = 0
    for babb in babbling:
        print(babb)
        for word in words:
            if word * 2 not in babb:
                babb = babb.replace(word, '')
            cnt += 1

    return cnt
print(solution(babbling))