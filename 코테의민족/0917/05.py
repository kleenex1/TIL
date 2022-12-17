P = int(input())
I = int(input())
S = input()

PN = 'I' + 'OI'*P 

l = len(PN)

count = 0
for i in range(I):
    if S[i:i+l] == PN:
        count += 1

print(count)

N = int(input())
M = int(input())
S = input()
answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)