from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from apps.stock.views import index
from apps.stock.views import create_product

urlpatterns = [
    path('', index, name='index'),
    path('create_product', create_product, name='create_product'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )