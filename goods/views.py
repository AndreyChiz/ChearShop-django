from django.shortcuts import render
from goods.goods_items import goods_items
from goods.models import Products
# Create your views here.
def catalog(request):
    goods = Products.objects.all().order_by('price')

    context = {
        "title": "Home - Каталог",
        "goods": goods
    }
    return render(request, 'goods/catalog.html', context)







def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }

    return render(request, 'goods/product.html', context=context)
