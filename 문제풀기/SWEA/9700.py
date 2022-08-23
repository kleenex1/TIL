import sys

sys.stdin = open("_USB꽂기.txt")

T = int(input())
for tc in range(1, T+1):
    p, q = map(float, input().split())
    
    # 올바른 면 p 확률
    # 올바른 면이면 q 꽂히고, 1-q 확률로 안꽂힘.
    # 뒤집어져 있으면 0  

    # 한번 뒤집었을때 꽂힐 확률 = ?
    
    # 들어갈 확률
    usb = p*q 
    # 1번 뒤집어서 들어갈 확률
    s1 = (1-p)*q
    # 2번 뒤집어서 들어갈 확률
    s2 = p*(1-q)*q
    print(f'#{tc}', "YES" if s1<s2 else "NO")
        