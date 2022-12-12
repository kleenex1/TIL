import sys 
sys.stdin = open("숭고한.txt")

univ = ["Soongsil", "Korea", "Hanyang"]

scores = list(map(int,input().split()))

if sum(scores) >= 100:
    print("OK")
else:
    answer = scores.index(min(scores))
    print(univ[answer])