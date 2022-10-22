import sys

sys.stdin = open("_UCPC.txt")

S = input()
alph = ['U', 'C', 'P', 'C']
valid = True

for a in alph:
    if a in S:
        S = S[S.index(a)+1:]
    else:
        valid = False
        break
if valid:
    print('I love UCPC')
else:
    print('I hate UCPC')