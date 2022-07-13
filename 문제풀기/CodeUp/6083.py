r, g, b = map(int, input().split())

count = 0
for red in range(0, r):
    for green in range(0, g):
        for blue in range(0, b):
            print(red, green, blue, sep=' ')
            
            count += 1

print(count)