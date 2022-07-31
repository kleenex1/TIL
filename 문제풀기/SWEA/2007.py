T = int(input())

for test_case in range(1, T + 1):
    word = input()
    
    madi = ''

    for i in range(len(word)):
        if word[:i+1] != word[i+1:i+i+2]:
            madi += word[i]
        else:
            madi += word[i]
            break
    
    print(len(madi))
