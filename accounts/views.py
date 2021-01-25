from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):

	form = RegisterForm()
	# form = UserCreationForm()

	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			# return HttpResponseRedirect("/")
			return redirect("/")

	return render(request, 'accounts/register.html', {'form':form})

def sign_in(request):

	form = LoginForm()

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			# return HttpResponseRedirect("/")
			return redirect("/")

	return render(request, 'accounts/login_page.html', {'form':form})

def log_out(request):
	logout(request)
	return redirect('/login')

