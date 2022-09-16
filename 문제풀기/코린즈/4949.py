import sys

sys.stdin = open("_균형잡힌세상.txt")

while True:
    S = input()
    if S == '.':
        break
    stack = []
    valid = 1
    for char in S:
        if char == "(" or char == "[":
            stack.append(char)
        if char == ")":
            if stack and stack[-1] == "(":
                stack.pop(-1)
            else:
                valid = 0
                break
        if char == "]":
            if stack and stack[-1] == "[":
                stack.pop(-1)
            else:
                valid = 0
                break
    if valid and not stack:
        print("yes")
    else:
        print("no")
    
# import sys
# sys.stdin = open("_균형잡힌세상.txt")
# from collections import deque

# try:
#   while True:
#     words = input()
#     # 열린 괄호 저장
#     open_ = []
#     # 닫힌 괄호 저장
#     close_ = []
#     # 똑바로 된 괄호 저장됐는지 확인
#     equal = []
#     # 공백제거
#     words = words.replace(" ", "")
#     # word에서 값을 추출하여 비교하기 위해 덱 사용
#     words_ = deque(list(words))
#     answer = "yes"
#     # 아무 문자가 없어도 no이므로
#     alpha = 0
    
#     for _ in range(len(words)):
#       # 현재 문자 추출
#       char = words_.popleft()
#       # 현재 문자가 괄호가 아닌 문자열이라면
#       # 문자열 1 증가
#       if char == '.':
#             # 온점이 들어오면 반복문 종료
#         break 
#       if char not in '[()]':
#         alpha += 1
#         # print(word)
#         # 괄호가 아닌 문자열이라면 다음 반복으로
#         continue
#       # print(char)
      
#       # 열린괄호라면 open에 추가
#       if char in '([':
#         open_.append(char)
#         # print(open_)
#       # 닫힌 괄호라면 open의 가장 마지막 값을 일단 꺼내서
#       # equal 리스트에 추가
#       elif char in '])':
#         if open_:
#           equal.append(open_.pop() + char)
          
#           # 열린 괄호가 없는데 닫힌 괄호가 나온다면
#           # 잉여 괄호에 추가하고 반복문 종료
#         else:
#           close_.append(char)
#           answer = "no"
#           break
        
#     # print(words_)
    
#     # 열린괄호와 닫힌괄호의 합이 0이 아니라면(딱 맞춰서 괄호가 닫히지 않았다면)
#     if len(open_) + len(open_) != 0:
#       answer = "no"
#     # 괄호가 올바른 괄호인지 검증
#     if equal:
#       for word in equal:
#         # 만약 괄호를 제외한 문자열이 하나도 없다면
#         # ([ (([( [ ] ) ( ) (( ))] )) ]).
#         # 괄호 성립 x
#         if not alpha:
#           answer = "no"
#           break
#         # 알맞는 짝이라면 괄호 성립
#         if word == '()' or word == '[]':
#           answer = "yes"
#         else:
#           answer = "no"
#           break

#     print(answer)
    
# except EOFError:
#   exit()