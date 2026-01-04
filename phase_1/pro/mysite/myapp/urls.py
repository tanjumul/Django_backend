from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('item/',views.item),
    path('blog/',views.writting),
    path('<int:id>/',views.details,name= 'detail'),
]

