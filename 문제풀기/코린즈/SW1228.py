import sys

sys.stdin = open("_암호문1.txt")


# for tc in range(1, 11):
#     N = int(input())
#     origin = list(map(int, input().split()))
#     M = int(input())
#     O = list(input().split())

#     for i in range(len(O)):
#         if O[i] == "I":
#             p = int(O[i+1])
#             x = int(O[i+2])
#             for j in range(x):
#                 origin.insert(p+j,O[i+2+j+1])
    
#     print("#{} {}".format(tc, ' '.join(map(str, origin[:10]))))

# for tc in range(1, 11):
#     N = int(input())
#     origin = list(map(int, input().split()))
#     M = int(input())
#     O = list(input().split())

#     for i in range(len(O)):
#         if O[i] == "I":
#             ans = []
#             p = int(O[i+1])
#             x = int(O[i+2])
#             for j in range(x):
#                 ans.append(O[i+2+j+1])
            
#             for i in ans[::-1]:
#                 origin.insert(p,i)

#     print("#{} {}".format(tc, ' '.join(map(str, origin[:10]))))

for t in range(1, 11):
  N = int(input())
  password = input().split()
    
  # 명령문
  M = int(input())
  order = input().split()
  # print(order)

  # 명령문을 돌면서 'I'가 발생할 때마다
  for idx in range(len(order)):
    if order[idx] == 'I':
      x = int(order[idx + 1])
      y = int(order[idx + 2])
      
      for how in range(y, 0, -1):
		# y가 5일 때, 5,4,3,2,1 까지의 인덱스 범위
        password.insert(x, order[idx + 2 + how]) 
        
  print(f'#{t}', end=" ")
  print(*password[:10])