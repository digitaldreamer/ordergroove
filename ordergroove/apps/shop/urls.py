from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^$', 'shop.views.index', name='shop_index'),
    url(r'^', include('shop.products.urls')),
)
