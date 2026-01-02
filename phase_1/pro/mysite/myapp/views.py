from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("Daily Blog Page : Tanjumul")


def item(request):
    return HttpResponse('This is an it section')

def writting(hobby):
    return HttpResponse('Blog site ')
    