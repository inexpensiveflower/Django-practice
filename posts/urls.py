# /posts/urls.py
from django.urls import path
# import views.py in current directory, this one will ne explained later
from . import views 

urlpatterns = [
    path('', views.index, name = "Index"),
]