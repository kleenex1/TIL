# N = int(input())
# card = list(map(int, input().split()))

# M = int(input())
# m_card = list(map(int, input().split()))

# answer = []
# for i in range(M):
#     answer.append(card.count(m_card[i]))

# print(answer)

## 시간초과 : O(N^2) , 주어진 값 --> 500,000

N = int(input())
card = map(int, input().split())

M = int(input())
m_card = map(int, input().split())

dict = {}

for n in card:
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1

for m in m_card:
    if m in dict:
        print(' '.join(str(dict[m])), end=' ')
    else:
        print('0', end=' ')
