from django.shortcuts import render
from django.http import HttpResponse
from . models import Item

# Create your views here.

def index(response):
    item_lists = Item.objects.all()
    return HttpResponse(item_lists)


def item(request):
    return HttpResponse('<h1>This is an it section</h1>')

def writting(hobby):
    return HttpResponse('Blog site ')

    