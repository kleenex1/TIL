import sys

T = int(sys.stdin.readline())

for _ in range(T):
    PS = sys.stdin.readline()
    
    list_ = []
    for P in PS:
        if P == "(":
            list_.append(P)
        elif P == ")":
            if list_:
                list_.pop()
            else:
                print("NO")
                break
    else:
        if not list_:
            print("YES")
        else:
            print("NO")

             