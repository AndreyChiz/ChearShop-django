from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from goods.models import Products


# Create your views here.
def catalog(request, category_slug):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None) # если не будет параметра то None
    order_by = request.GET.get('order_by', None) # аналогично

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

# фильтры
    if on_sale: #если сработат то к goods применится
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default': #если сработат то к goods применится
        goods = goods.order_by(order_by)


    paginator = Paginator(goods, 3) # goods в любом случае проходит через пагинатор
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slag_url": category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug, ):
    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }

    return render(request, 'goods/product.html', context=context)
