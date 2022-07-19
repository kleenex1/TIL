def gugudan(num):
    for i in range(num, num + 1):
        for j in range(1, 9+1):
            print("{} * {} = {}".format(i, j, i*j))
    
if __name__== "__main__":
    num = int(input())
    gugudan(num)