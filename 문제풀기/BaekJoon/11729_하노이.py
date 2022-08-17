# 하노이 탑 
# 세개의 장대가 있고 
# 한 번에 한 개의 원판만 이동
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

def move_disk(disk_num, start, end):
    print("{} {}".format(start, end))

def hanoi(num, start, end):
    hanoi_sub(num, start, end, 2)

def hanoi_sub(N, start, end, other):
    if N == 1:
        move_disk(1, start, end)
    else:
        hanoi_sub(N-1, start, other, end)
        move_disk(N, start, end)
        hanoi_sub(N-1, other, end, start)

N = int(input())
print(2**N-1)
hanoi(N,1,3)


# def hanoi_tower(n, start, end) :
#     if n == 1 :
#         print(start, end)
#         return
       
#     hanoi_tower(n-1, start, 6-start-end) # 1단계
#     print(start, end) # 2단계
#     hanoi_tower(n-1, 6-start-end, end) # 3단계
    
# n = int(input())
# print(2**n-1)
# hanoi_tower(n, 1, 3)