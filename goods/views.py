from django.shortcuts import render
from goods.goods_items import goods_items
# Create your views here.
def catalog(request):
    context = {
        "title": "Home - Каталог",
        "goods": goods_items
    }
    return render(request, 'goods/catalog.html', context)



def product(request):
    return render(request, 'goods/product.html')

