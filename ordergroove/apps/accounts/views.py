from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def dashboard(request, template='accounts/dashboard.html'):
    context = {
        'section': 'account',
        'page': 'accounts_dashboard',
        'user': request.user,
    }
    return render(request, template, context)
