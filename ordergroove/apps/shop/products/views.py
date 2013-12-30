from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from ordergroove import Breadcrumb
from shop.products.models import Category


def _breadcrumbs():
    breadcrumbs = [
        Breadcrumb('Home', reverse('home')),
        Breadcrumb('Shop', reverse('shop_index')),
    ]
    return breadcrumbs

def category(request, category_slug, template='shop/products/category.html'):
    category = get_object_or_404(Category, slug=category_slug)
    breadcrumbs = _breadcrumbs()
    breadcrumbs.append(Breadcrumb(category.name, category.get_absolute_url()))

    if not category.active:
        try:
            del request.session['breadcrumbs']
        except KeyError:
            pass

        raise Http404()
    else:
        request.session['breadcrumbs'] = breadcrumbs

    context = {
        'section': 'shop',
        'page': 'category',
        'breadcrumbs': breadcrumbs,
        'category': category,
    }
    return render(request, template, context)
