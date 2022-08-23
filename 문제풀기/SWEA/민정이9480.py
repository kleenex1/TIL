import sys

sys.stdin = open("_민정이.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

# 광직이가 N개의 단어를 알고 있고, 이 중 몇개를 골라서 하나의 세트로만드는데
# 단어 세트에는 26개의 알파벳 소문자가 모두포함되어야함
# 모든 알파벳 소문자에 대해 단어 세트 안에 그 문자를 포함하는 단어가..
# 서로 다른 세트를 많이 만들어 주려고 한다
    words = [list(input()) for _ in range(N)]

    print(words)        