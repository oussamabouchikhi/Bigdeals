from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from .models import Product

def product_list(request):
     # get all products
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 1) #Show 16 products per page.
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)

    # to let django know that 'product_list' is this function so we can use it in templates
    context = {
        'product_list': product_list,
    }
    return render(request, 'Product/product_list.html', context)



def product_details(request, slug):
    # get product which has this slug
    product_details = Product.objects.get(prodSlug=slug)
    context = {
        'product_details': product_details,
    }
    return render(request, 'Product/product_details.html', context)
