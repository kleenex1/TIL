# N, X = map(int, input().split())
# A = map(int, input().split())
# B = list(A)
# result = ''
# for i in range(N):
#     if B[i] < X:
#         result += str(B[i]) + " " 
    
# print(result)

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

left = set()
for i in range(10):
    a = int(input())
    left.add(a % 42)
print(len(left))

