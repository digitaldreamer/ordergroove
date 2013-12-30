import copy

from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from ordergroove import Breadcrumb
from shop.products.models import Category, Product


def _breadcrumbs():
    breadcrumbs = [
        Breadcrumb('Home', reverse('home')),
        Breadcrumb('Shop', reverse('shop_index')),
    ]
    return breadcrumbs

def category(request, category_slug, template='shop/products/category.html'):
    site = Site.objects.get_current()
    category = get_object_or_404(Category, site=site, slug=category_slug, active=True)

    # breadcrumbs
    breadcrumbs = _breadcrumbs()
    breadcrumbs.append(Breadcrumb(category.name, category.get_absolute_url()))

    # set the session for the product pages
    request.session['category_id'] = category.id

    context = {
        'section': 'shop',
        'page': 'category',
        'breadcrumbs': breadcrumbs,
        'category': category,
    }
    return render(request, template, context)


def product(request, product_slug, template='shop/products/product.html'):
    site = Site.objects.get_current()
    product = get_object_or_404(Product, site=site, slug=product_slug, active=True)
    breadcrumbs = _breadcrumbs()
    category = product.main_category

    # override category if it's set in the session
    try:
        category_id = request.session['category_id']
    except KeyError:
        pass
    else:
        if category_id:
            category = Category.objects.get(id=category_id)

    # build breadcrumbs
    if category:
        breadcrumbs.append(Breadcrumb(category.name, category.get_absolute_url()))
    breadcrumbs.append(Breadcrumb(product.name, product.get_absolute_url()))

    context = {
        'section': 'shop',
        'page': 'product',
        'breadcrumbs': breadcrumbs,
        'category': category,
        'product': product,
    }
    return render(request, template, context)
