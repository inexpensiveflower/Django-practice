from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.register, name = 'Register'),
	path('login/', views.log_in, name = 'Login'),
	path('logout/', views.log_out, name = 'Logout'),
	path('', views.index, name = 'Account_Index')
]