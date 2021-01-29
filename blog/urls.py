from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name = 'post_list'),
	# <int:pk> means that Django will obtain an integer and transfer it to a variable called pk for view
	# For example, if typing http://127.0.0.1/post/5 on browser, Django will pass variable pk = 5 to corresponding view
	path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
	path('post/new/', views.post_new, name = 'post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
	path('post/<int:pk>/delete/', views.post_delete, name = 'post_delete'),
]