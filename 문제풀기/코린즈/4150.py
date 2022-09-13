def fib(n):
    fib_table = [0,1,1]
    
    for i in range(3, n+1):
        fib_table.append(fib_table[i-1]+fib_table[i-2])

    return fib_table[n]

N = int(input())
print(fib(N))