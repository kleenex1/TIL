word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
for i in range(len(word)):
    result = result + str(ord(word[i])-64) + " "

print(result)