from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("Daily Blog Page : Tanjumul")


def item(request):
    return HttpResponse('<h1>This is an it section</h1>')

def writting(hobby):
    return HttpResponse('Blog site ')

    