from django.shortcuts import render
import random
# Create your views here.


def lotto(request):
    lotto_list = [] # 리스트
    bonus, *lotto_winner = random.sample(range(1,46),7)
    

    for _ in range(5):
        lotto = random.sample(range(1,46),6) # 리스트
        count = 0
        result = 0 # 등수
        for num in lotto:
            if num in lotto_winner:
                count += 1

        if count == 3:
            result = 5
        elif count == 4:
            result = 4
        elif count == 5:
            if bonus not in lotto:
                result = 3
            else:
                result = 2
        elif count == 6:
            result = 1

        lotto_list.append((lotto,result))
       

    context = {
        "lotto_winner" : lotto_winner,
        "bonus" : bonus,
        "lotto_list": lotto_list,
    }

    return render(request, 'lottos/lotto.html', context)