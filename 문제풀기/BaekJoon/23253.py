from sys import stdin

N, M = map(int, stdin.readline().split())
answer = {
        "No":0
        }
for _ in range(M):
    stdin.readline()
    items = list(map(int, stdin.readline().split()))

    
    for i in range(len(items)-1):
        if items[i] < items[i+1]:
            answer["No"] += 1
            break
    
print("Yes" if answer["No"] == 0 else "No")