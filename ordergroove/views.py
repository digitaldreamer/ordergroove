from django.shortcuts import render


def home(request, template='index.html'):
    context = {}
    return render(request, template, context)
