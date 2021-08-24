from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def controller(request):
    return render(request, 'controller.html')


def water_settings(request):
    return render(request, 'settings.html')


def configurations(request):
    return render(request, 'configurations.html')