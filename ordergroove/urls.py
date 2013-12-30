from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ordergroove.views.home', name='home'),
    url(r'^account/', include('accounts.urls')),
    url(r'^registration/', include('registration.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
