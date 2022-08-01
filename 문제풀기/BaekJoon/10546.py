import sys 

n = int(sys.stdin.readline())

names = dict()
for i in range(n):
    name = sys.stdin.readline()
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

for i in range(n-1):
    name = sys.stdin.readline()
    if name in names:
        names[name] -= 1

for name in names:
    if names[name] :
        print(name)
        break
