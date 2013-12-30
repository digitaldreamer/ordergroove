from django.shortcuts import render


def home(request, template='index.html'):
    context = {
        'section': 'index'
    }
    return render(request, template, context)
