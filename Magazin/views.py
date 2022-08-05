from django.shortcuts import render
from Magazin.models import Product



def index(request):
    dict_ = {
        'Ablai': 'Privet',
        'Aba': 'Hello',
        'name': ['abali', 'Aba', 'Ababubich']
}
    return render(request, 'index.html', context=dict_)


def product_list_view(request):
    products = Product.objects.all() #QuerySet
    context = {
        'product_list': products
    }
    print(products)
    return render(request, 'products.html', context=context)


def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', context={'product_detail': product})
# Create your views here.