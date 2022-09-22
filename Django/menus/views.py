from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'menus/index.html')

dinners = [('삼겹살','https://cdn.mindgil.com/news/photo/202103/70839_7148_1250.jpg'),
('짜장면','https://i.ytimg.com/vi/Yn8ZFTBCJJQ/maxresdefault.jpg'),
('떡볶이','http://img4.tmon.kr/cdn3/deals/2021/07/15/4500036162/original_4500036162_front_f8dfd_1626343427production.jpg')
]


def dinner(request):
    name, img = random.choice(dinners)
    context = {
        'name' : name,
        'img' : img, 
    }
    return render(request, 'menus/today-dinner.html', context)

