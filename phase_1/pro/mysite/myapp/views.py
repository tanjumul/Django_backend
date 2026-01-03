from django.shortcuts import render
from django.http import HttpResponse
from . models import Item

# Create your views here.

def index(response):
    #getting items from the database
    item_list = Item.objects.all()
    #creating a context using lists
    context ={ 
              'item_list': item_list
              }
    # return HttpResponse(item_lists)
    #passing the context object to the render method along the rest
    return render(response,"myapp/index.html",context)



def details(response,id): 
           item = Item.objects.get(id=id) 
           context = { 
                      'item':item #here item is the variable of the database here see in the upper line
                      }
           return render(response,'myapp/detail.html',context)
       
           #return HttpResponse(f'This is details of {item}')




def item(request):
    return HttpResponse('<h1>This is an it section</h1>')

def writting(hobby):
    return HttpResponse('Blog site ')

    