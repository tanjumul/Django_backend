from django.shortcuts import render
from django.http import HttpResponse
from . models import Item

# Create your views here.

def index(response):
    #taking data from database
    item_list = Item.objects.all()
    #making a context using lists
    context ={ 
              'item_list': item_list
              }
    # return HttpResponse(item_lists)
    #returing as render from the html page from templete section
    return render(response,"myapp/index.html",context)

def item(request):
    return HttpResponse('<h1>This is an it section</h1>')

def writting(hobby):
    return HttpResponse('Blog site ')

    