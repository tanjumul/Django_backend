from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('item/',views.item),
    path('blog/',views.writting),
    path('<int:id>/',views.details)
]

