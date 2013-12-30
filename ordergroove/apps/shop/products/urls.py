from django.conf.urls import patterns, include, url

urlpatterns = patterns('shop.products.views',
    url(r'^category/(?P<category_slug>[\w-]+)/$', 'category', name='shop_products_category'),
    url(r'^product/(?P<product_slug>[\w-]+)/$', 'product', name='shop_products_product'),
)
