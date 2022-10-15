import sys

sys.stdin = open('_최댓값과최솟값.txt')

s = input()
def solution(s):
    lst = []
    result = s.split(" ")
    for i in result:
        lst.append(int(i))
        
    return (f'{str(min(lst))} {str(max(lst))}')

print(solution(s))