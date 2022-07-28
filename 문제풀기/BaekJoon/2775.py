N = int(input())

for _ in range(N):
    floor = int(input())
    num = int(input())
    ground = [x for x in range(1, num + 1)]
    
    for k in range(floor):
        for i in range(1, num):
            ground[i] += ground[i-1]
        
    print(ground[-1])
