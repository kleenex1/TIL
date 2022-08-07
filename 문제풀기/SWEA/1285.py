T = int(input())

for test_case in range(1, T + 1):
    people = int(input())
    record = list(map(int, input().split()))
    
    record_abs = [abs(x) for x in record]
    
    min_ = record_abs[0]
    
    for i in record_abs:
        if i <= min_:
            min_ = i
    
    count_ = record_abs.count(min_)      
     
    print('#{} {} {}'.format(test_case, min_, count_))