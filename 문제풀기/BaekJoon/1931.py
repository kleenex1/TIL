import sys

sys.stdin = open("_회의실배정.txt")

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
    
schedules = sorted(meetings, key=lambda x:(x[1],x[0]))

s = [schedules[0]]

for i in range(1,len(schedules)):
    if schedules[i][0] >= s[-1][1]:
        s.append(schedules[i])
    
print(len(s))