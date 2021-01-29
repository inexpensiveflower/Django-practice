from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Index'),
    path('update/<str:pk>', views.update, name = "Update"),
    path('delete/<str:pk>', views.delete, name = "Delete"),
]