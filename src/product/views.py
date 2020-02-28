from django.shortcuts import render

# Create your views here.
from .models import Product

def product_list(request):
    # to let django know that 'product_list' is this function so we can use it in templates
    context = {
        'product_list': product_list,
    }
    return render(request, 'Product/product_list.html', context)



def product_details(request, id):
    # get product which has this id
    product_details = Product.objects.get(id=id)
    context = {
        'product_details': product_details,
    }
    return render(request, 'Product/product_details.html', context)
