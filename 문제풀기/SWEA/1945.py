T = int(input())

for test_case in range(1, T + 1):
    nums = int(input())
    num = [2, 3, 5, 7, 11]
    count_ = [0, 0, 0, 0, 0]

    for i in range(len(num)):

        while True:
            if nums % num[i] == 0:
                nums = nums//num[i]
                count_[i] += 1
            else:
                break
    
    print('#{} {}'.format(test_case, ' '.join(map(str, count_))))
