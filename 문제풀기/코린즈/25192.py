import sys

sys.stdin = open("_인사성밝은곰곰이.txt")
input = sys.stdin.readline
N = int(input())

gom = dict()
answer = 0
for i in range(N):
    S = input()
    if S == "ENTER":
        answer += sum(gom.values())
        gom = dict()
    else:
        gom[S] = 1

answer += sum(gom.values())
print(answer)


