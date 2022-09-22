from django.shortcuts import render
import random
# Create your views here.

numbers = range(1,46)

def lotto(request):
    prize = random.sample(numbers,7)
    num = random.sample(numbers,6)
    num1 = random.sample(numbers,6)
    num2 = random.sample(numbers,6)
    num3 = random.sample(numbers,6)
    num4 = random.sample(numbers,6)

    context = {
        'prize': prize,
        'num': num,
        'num1': num1,
        'num2': num2,
        'num3': num3,
        'num4': num4,
    }
    return render(request, 'lottos/lotto.html', context)