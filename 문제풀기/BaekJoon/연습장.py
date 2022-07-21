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

n = int(input())
num = input()
total = 0
for i in range(n):
    total += int(i)
print(total)