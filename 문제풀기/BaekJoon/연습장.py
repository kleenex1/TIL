# N, X = map(int, input().split())
# A = map(int, input().split())
# B = list(A)
# result = ''
# for i in range(N):
#     if B[i] < X:
#         result += str(B[i]) + " " 
    
# print(result)

# def dice_prize(dice_numbers):
#     price = 0
#     if len(set(dice_numbers)) == 1:
#         price = 10000 + dice_numbers[0] * 1000
#     elif len(set(dice_numbers)) == 3:
#         price = max(dice_numbers) * 100
#     else:
#         price = 1000 + (sum(dice_numbers)- sum(list(set(dice_numbers)))) * 100    

#     return price


# if __name__ == "__main__":
#     dice_numbers = list(map(int, input().split()))
#     print(dice_prize(dice_numbers))
    
    

# a,b = map(int,input().split())
# score = [x for x in input().split() if int(x)<b]
# print(' '.join(score))

# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A + B)
#     except:
#         break


# n = int(input())
# num = n
# count = 0
# while True:
#     a = num // 10
#     b = num % 10
#     c = (a + b) % 10
#     num = (b*10) + c
#     count += 1
#     if num == n:
#         break
# print(count)
    
# n = input()
# num = n
# count = 0
# while 1:
#     if len(num) == 1:
#         num = "0" + num
#     plus = str(int(num[0]) + int(num[1]))
#     num = num[-1] + plus[-1]
#     count += 1
#     if num == n:
#         print(count)
#         break

# num = []
# for i in range(9):
#     a = int(input())
#     num.append(a)
# print(max(num))
# print(num.index(max(num))+1)

# A = int(input())
# B = int(input())
# C = int(input())

# number = list(str((A * B * C)))

# answer = [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0]

# for num in number:
#     answer[int(num)] += 1

# for ans in answer:
#     print(ans)

# left = set()
# for i in range(10):
#     a = int(input())
#     left.add(a % 42)
# print(len(left))

# n = int(input())
# score = list(map(int, input().split()))
# total = 0
# for i in score:
#     if i == max(score):
#         total += 100
#     else:
#         total += (i / max(score)) * 100

# print(total/n)

# n = int(input())
# for i in range(n):
#     quiz = input()
#     point = 0
#     total = 0
#     for i in range(len(quiz)):
#         if quiz[i] == 'O':
#             point += 1
#             total += point
#         else:
#             point = 0
#     print(total)

# n = int(input())
# for i in range(n):
#     student = list(map(int, input().split()))
#     avg = sum(student[1:]) / (len(student)-1)
#     point_student = student[1:]
#     count = 0
#     for point in point_student:
#         if avg < point:
#             count += 1
#     print("{:.3f}%".format((count/student[0])*100))

# natural_num = set(range(1, 10001))
# generated_num = set()

# for i in range(1, 10001):
#     for j in str(i):
#         i += int(j)
#     generated_num.add(i)

# self_num = sorted(natural_num - generated_num)
# for i in self_num:
#     print(i)



# def hansu(n):
#     hansu_count = 0
#     for i in range(1, n + 1):
#         num = list(map(int, str(i)))
#         if i < 100:
#             hansu_count += 1
#         elif num[0] - num[1] == num[1] - num[2]:
#             hansu_count += 1

#     return hansu_count
# print(hansu(1000))


# word = 'baekjoon'

# for i in range(97, 122 +1):
#     if chr(i) in word:
#         print(word.find(chr(i)), end=' ')
#     else:
#         print(-1, end= ' ')

# T = int(input())

# for test_case in range(T):
#     a, b = map(str, input().split())
#     for chr in b:
#         print(chr*int(a), end='')
#     print()



"""
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    count = word.count # 메서드를 호출하지 않고 변수에 넣어둔다.. 팁
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")

else:
    print(word_list[(cnt.index(max(cnt)))]) # 리스트와 인덱스.. 팁
"""


# a, b = map(str, input().split())

# print(max(int(a[::-1]), int(b[::-1])))


# dials = [
#     'ABC',
#     'DEF',
#     'GHI',
#     'JKL',
#     'MNO',
#     'PQRS',
#     'TUV',
#     'WXYZ'
# ]
# second = 0
# word = input()
# for char in word:
#     for dial in dials:
#         if char in dial:
#            second += dials.index(dial) + 3
# print(second)


# n = int(input())

# for i in range(n):
#     if i % 2 == 0:
#         print("* " * n)
#     else:
#         print(" *" * n)

# 하나씩 불러내서 다시 연결하면서 해당 단어가 크로아티아 알파벳이면 +1 아니면 그냥 +1

'''
word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for char in croatia:
    word = word.replace(char, '*')   # replace는 비파괴적 함수..
print(len(word))
'''



# T = int(input())

# for test_case in range(1, T+1):
#     date = input()
#     even_month =  ['02', '04', '06', '08', '10', '12']
#     odd_month = ['01', '03', '05', '07', '09', '11']
#     month_list = even_month + odd_month
#     month_date = list(range(1,32))
#     even_month = list(map(str, month_date[:31]))
#     odd_month = list(map(str, month_date[:30]))
#     feburary = list(map(str, month_date[:28]))
#     if date[4:6] not in month_list:
#         print(f'#{test_case} -1')
        
#     elif date[4:6] == '02' and date[6:] not in feburary:
#         print(f'#{test_case} -1')
        
#     elif date[4:6] in even_month and date[6:] not in even_month:
#         print(f'#{test_case} -1')
        
#     elif date[4:6] in odd_month and date[6:] not in odd_month:
#         print(f'#{test_case} -1')
        
#     else:
#         print(f'#{test_case} {date[:4]}/{date[4:6]}/{date[6:]}')

# word = input()

# print(word.upper()) # 문자만 알아서 되는듯..

# https://www.acmicpc.net/problem/2577



# T = int(input())
# total = 0
# for _ in range(T):
#     word = input()
#     for i in range(len(word)):   
#         if i != len(word)-1:
#             if word[i] == word[i+1]:
#                 pass
#             elif word[i] in word[i+1:]:
#                 break
#     #   total += 1 
#         else:
#             total += 1    
# print(total)

# a, b, c= map(int, input().split())
# if b >= c:
#     print(-1)
# else:
#     print((a // (c- b)) +1)


# A, B = map(int, input().split())

# print("A" if A>B else "B")


# [1/1] [1/2, 2/1] [3/1, 2/2, 1/3] [1/4, 2/3, 3/2, 4/1]

# X = int(input())

# line = 1
# while X > line:
#     X -= line 
#     line += 1

# if line % 2 == 0:
#     a = X
#     b = line - X + 1
# else:
#     a = line - X + 1
#     b = X
# print(a, '/', b, sep='')


# a, b, v = map(int, input().split())
# k = (v - b)/(a - b)
# print(int(k) if k == int(k) else int(k) + 1 )

# n =list(map(str, input()))
# left = 0
# right = 0
        
# for i in range(len(n)):
#     if n[i] == '0':
#         left = n[:i].count("@")
#         right = n[i:].count("@")

# print(left, right)


# word = list(map(str, 'CAMBRIDGE'))


# input_ = input()

# for char in input_:
#     if char in word:
#         input_ = input_.replace(char,"")

# print(input_)

# N = int(input())

# for i in range(N):
#     n, word = input().split()
#     word_list = list(map(str, word))
#     del word_list[int(n)-1]
#     print(''.join(word_list))


# jangjo = list(map(int, input().split()))


# if jangjo == sorted(jangjo):
#     print("ascending")
# elif jangjo == sorted(jangjo, reverse = True):
#     print("descending")
# else:
#     print("mixed")

# all_num = set((range(1,10000+1)))
# not_self_num = set()

# for i in range(1,10000 + 1):
#     for j in str(i):
#         i += int(j)
#     not_self_num.add(i)

# self_num = sorted(all_num - not_self_num)
# for i in self_num:
#     print(i)

# set는 교집합 & 합집합 + 차집합 - 가능.. 



# from typing import List # 타입힌트 List 
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
#         return s

# s = ["h", "e", "l", "l", "o"]
# print(Solution().reverseString(s))


class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    def __init__(self):
        self.scoops = []
    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)

s1 = Scoop('Chocolate')
s2 = Scoop('Vanilla')
s3 = Scoop('Persimmon')

b = Bowl()
b.add_scoops(s1, s2, s3)
print(b)