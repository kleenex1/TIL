# 시간초과
# words = input()
# bomb = input()
# while bomb in words:
#     words = words.replace(bomb, "")

# if not words:
#     print("FRULA")
# else:
#     print(words)

words = input()
bomb = input()

stack = []
for word in words:
    stack.append(word)
    if word == bomb[-1] and "".join(stack[-(len(bomb)):]) == bomb:
        del stack[-(len(bomb)):]

answer = "".join(stack)

if not answer:
    print("FRULA")
else:
    print(answer)