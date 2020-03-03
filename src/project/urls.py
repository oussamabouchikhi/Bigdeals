"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

"""
path('', include('product.urls', namespace='products')),
when you open admin panel 'http://127.0.0.1:8000/admin/'
django will think admin is a slug [if you're usnig slug as url]
so to resolve this problem we use 'products/' instead of leaving it empty
'' => 'http://127.0.0.1:8000/'
'products/' => 'http://127.0.0.1:8000/products/' : main products page
"""

urlpatterns = [
    # 'http://127.0.0.1:8000/admin/'
    path('admin/', admin.site.urls),
    # 'http://127.0.0.1:8000/products/'
    path('products/', include('product.urls', namespace='products')),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
