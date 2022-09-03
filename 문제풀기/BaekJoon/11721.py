import sys

sys.stdin = open("_열개씩.txt")

words = input()

for i in range(0,len(words),10):
    print(words[i:i+10])

