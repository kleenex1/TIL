import sys

sys.stdin = open("_암기왕.txt")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    N_memo = set(map(int,input().split()))
    M = int(input())
    M_memo = list(map(int, input().split()))
    
    for i in M_memo:
        if i in N_memo:
            print(1)
        else:
            print(0)
# T = int(input())
# for t in range(T):
#     N = int(input())
#     note1 = input().split()
#     M = int(input())
#     note2 = input().split()
#     res = []
#     num_dict = dict()
#     for n in note1:
#         num_dict[n] = '1'
#     for n in note2:
#         res.append(num_dict.get(n, '0'))
#     print('\n'.join(res))