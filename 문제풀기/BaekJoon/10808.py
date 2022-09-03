import sys

sys.stdin = open("_알파벳개수.txt")

S = input()

alphabet = [0]*26

for i in S:
    alphabet[ord(i)-97] += 1

print(' '.join(map(str, alphabet)))