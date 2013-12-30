from django.conf import settings
from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.forms.util import ErrorList
from django.http import HttpResponseRedirect
from django.shortcuts import render

from registration import create_user
from registration.forms import LoginForm, RegistrationForm


# Create your views here.
def login(request, Form=LoginForm, template='registration/login.html'):
    """
    user login

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

                # redirect user
                if next:
                    return HttpResponseRedirect(next)
                else:
                    return HttpResponseRedirect(reverse(settings.REGISTRATION['LOGIN_REDIRECT']))
            else:
                # the user failed to auth or is inactive
                errors = form._errors.setdefault('__all__', ErrorList())
                errors.append('Login Failed')
    else:
        form = Form()

    context = {
        'section': 'registration',
        'form': form,
        'next': next,
    }
    return render(request, template, context)


def logout(request, template='registration/logout.html'):
    """
    user logout

    use `next` GET param to override REGISTRATION['LOGOUT_REDIRECT']
    """
    next = request.GET.get('next', '')
    LOGOUT_REDIRECT = settings.REGISTRATION['LOGOUT_REDIRECT']
    context = {
        'section': 'registration_logout',
    }

    _logout(request)

    # redirect the user
    # ignore if registration_logout was requested
    if LOGOUT_REDIRECT != 'registration_logout':
        if next:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(reverse(settings.REGISTRATION['LOGOUT_REDIRECT']))

    return render(request, template, context)


def register(request, Form=RegistrationForm, template="registration/register.html"):
    """
    user registration

    use `next` GET param to override REGISTRATION['REGISTER_REDIRECT']
    """
    next = request.GET.get('next', '')

    if request.POST:
        form = Form(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            # TODO: check if we need to confirm email or not

            # create and log in user
            user = create_user(
                cleaned_data['username'],
                cleaned_data['email'],
                cleaned_data['password1'],
                first_name = cleaned_data['first_name'],
                last_name = cleaned_data['last_name']
            )

            # I know the password is correct so skip authentication and log in
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            _login(request, user)

            # redirect
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse(settings.REGISTRATION['REGISTER_REDIRECT']))
    else:
        form = Form()

    context = {
        'section': 'registration',
        'form': form,
        'next': next,
    }

    return render(request, template, context)


def register_complete(request, template='registration/register_complete.html'):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))

    context = {
        'section': 'registration',
    }
    return render(request, template, context)
