from django.conf.urls import *

# place app url patterns here
urlpatterns = patterns('accounts.views',
    url(r'^$', 'dashboard', name='accounts_dashboard'),
)
