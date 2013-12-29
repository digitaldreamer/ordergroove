from django.conf import settings
from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.core.urlresolvers import reverse
from django.forms.util import ErrorList
from django.http import HttpResponseRedirect
from django.shortcuts import render

from registration.forms import LoginForm


# Create your views here.
def login(request, Form=LoginForm, template='registration/login.html'):
    """
    Process user login

    use `next` GET param to override REGISTRATION['LOGIN_REDIRECT']
    """
    next = request.GET.get('next', '')

    if request.POST:
        form = Form(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            password = cleaned_data['password']
            user = authenticate(username=username, password=password)

            # check if the user was authenticated
            if user and user.is_active:
                _login(request, user)

                if next:
                    return HttpResponseRedirect(next)
                else:
                    return HttpResponseRedirect(reverse(settings.REGISTRATION['LOGIN_REDIRECT']))
            else:
                # the user failed to auth or is inactive
                errors = form._errors.setdefault('__all__', ErrorList())
                errors.append('Login Failed')
        else:
            # the form failed to validate
            pass
    else:
        form = Form()

    context = {
        'form': form
    }
    return render(request, template, context)


def logout(request, template='registration/logout.html'):
    """
    Process user logout

    use `next` GET param to override REGISTRATION['LOGOUT_REDIRECT']
    """
    next = request.GET.get('next', '')
    LOGOUT_REDIRECT = settings.REGISTRATION['LOGOUT_REDIRECT']
    context = {}

    _logout(request)

    # redirect the user
    # ignore if registration_logout was requested
    if LOGOUT_REDIRECT != 'registration_logout':
        if next:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(reverse(settings.REGISTRATION['LOGOUT_REDIRECT']))

    return render(request, template, context)
