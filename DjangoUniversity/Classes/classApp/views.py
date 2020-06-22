from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    classes = {}
    context = {
        'classes': classes,
    }
    return render(request, "home.html", context)
