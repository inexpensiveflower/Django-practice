from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm, CustomerModelForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'Login')
def index(request):

	form = CustomerModelForm()
	if request.method == "POST":
		form = CustomerModelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/accounts/")

	return render(request, 'accounts/index.html', {'form':form})

def register(request):

	form = RegisterForm()
	# form = UserCreationForm()

	if request.method == "POST":
		form = RegisterForm(request.POST)
		# form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			# the index page depends on which app to redirect.
			return redirect("/expenses/")

	return render(request, 'accounts/register.html', {'form':form})

def log_in(request):

	form = LoginForm()

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			# the index page depends on which app to redirect.
			return redirect("/expenses/")

	return render(request, 'accounts/login_page.html', {'form':form, 'source':request.get_full_path()})

def log_out(request):
	logout(request)
	return redirect('/accounts/login')

