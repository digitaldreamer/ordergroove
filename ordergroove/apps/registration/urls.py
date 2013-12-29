try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *


# place app url patterns here
urlpatterns = patterns('registration.views',
    url(r'^login/$', 'login', name='registration_login'),
    url(r'^logout/$', 'logout', name='registration_logout'),
)
