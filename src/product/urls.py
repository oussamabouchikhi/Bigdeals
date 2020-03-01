from django.urls import path
from . import views

app_name = "product"

urlpatterns = [

    path('', views.product_list),
    path('<int:id>', views.product_details, name='product_detail'),

]
