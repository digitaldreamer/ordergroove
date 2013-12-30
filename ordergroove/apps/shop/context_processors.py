def shop_context(request):
    context = {}
    context.update(_products(request))
    return context

def _products(request):
    from shop.products.models import Category

    return {
        'root_categories': Category.root_categories()
    }

