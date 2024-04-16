from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world!")


def user(request):
    return HttpResponse("Hello, user!")


def python(request):
    return HttpResponse("Hello, Python!")


def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
