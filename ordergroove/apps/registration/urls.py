from django.conf.urls import *

# place app url patterns here
urlpatterns = patterns('registration.views',
    url(r'^login/$', 'login', name='registration_login'),
    url(r'^logout/$', 'logout', name='registration_logout'),
    url(r'^register/$', 'register', name='registration_register'),
    url(r'^register/complete/$', 'register_complete', name='registration_register_complete'),
)
