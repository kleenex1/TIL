import sys

sys.stdin = open('_상금헌터.txt')

# code1 = [500,300,200,50,30,10]
# code1_rank = [1,3,6,10,15,21]

# code2 = [512,256,128,64,32]
# code2_rank = [1,3,7,15,31]


# T = int(input())
# for _ in range(T):
#     prize_A = []
#     prize_B = []
#     a, b = map(int, input().split())
#     for i in code1_rank:
#         if a > 21 or a == 0:
#             prize_A = [0]
#         elif a <= i:
#             prize_A.append(code1[code1_rank.index(i)])

#     for i in code2_rank:
#         if b > 31 or b == 0:
#             prize_B = [0]
#         elif b <= i:
#             prize_B.append(code2[code2_rank.index(i)])

#     print((max(prize_A)+max(prize_B))*10000)


prevPrize,prize = (500,300,200,50,30,10),(512,256,128,64,32)
prevFes = [0] + [prevPrize[i] for i in range(6) for _ in range(i+1)]
fes = [0] + [prize[i] for i in range(5) for _ in range(2**i)]

for _ in range(int(input())):
    a,b = map(int,input().split())
    if a >= len(prevFes):
        a = 0
    if b >= len(fes):
        b = 0
    print((prevFes[a] + fes[b])*10000)