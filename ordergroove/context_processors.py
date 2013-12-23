from django.conf import settings

def main_context(request):
    context = {}
    context.update(_settings(request))
    return context

def _settings(request):
    from django.contrib.sites.models import Site

    return {
        'MEDIA_VERSION': settings.MEDIA_VERSION,
        'site': Site.objects.get(id=settings.SITE_ID),
    }

