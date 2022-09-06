import sys

sys.stdin = open("_회사에있는사람.txt")

N = int(input())
company = dict()
for i in range(N):
    e, s = input().split()
    company[e] = s

answer = sorted(company.items(), reverse=True)
for k,v in answer:
    if v == "enter":
        print(k)
