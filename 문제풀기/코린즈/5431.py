import sys

sys.stdin = open("_민석이과제체크.txt")

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    students = list(map(int, input().split()))
  
    result = filter(lambda x: x not in students, list(range(1,N+1)))
    print('#{} {}'.format(tc, ' '.join(list(map(str, result)))))
    # unsubmit = []
    # for i in range(1,N+1):
    #     if i not in students:
    #         unsubmit.append(str(i))
    
    # print('#{} {}'.format(tc, ' '.join(unsubmit)))