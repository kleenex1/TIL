import sys

sys.stdin = open("_고무오리디버깅.txt", encoding="UTF8")

S = []
while True:
    N = input()
    if N == '문제':
        S.append('문제')
    if N == "고무오리":
        if not S:
            S.append("문제")
            S.append("문제")
        else:
            S.pop()
    if N == "고무오리 디버깅 끝":
        break

if S:
    print("힝구")
else:
    print("고무오리야 사랑해")
