from django.core.urlresolvers import reverse
from django.shortcuts import render
from ordergroove import Breadcrumb


def _breadcrumbs():
    breadcrumbs = [
        Breadcrumb('Home', reverse('home')),
    ]
    return breadcrumbs

# Create your views here.
def index(request, template='shop/index.html'):
    request.session['category_id'] = None

    context = {
        'section': 'shop',
        'breadcrumbs': _breadcrumbs(),
    }
    return render(request, template, context)
