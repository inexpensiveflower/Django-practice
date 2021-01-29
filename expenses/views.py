from django.shortcuts import render, redirect
from .forms import ExpenseModelForm
from .models import Expense
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'Login')
def index(request):

	expenses = Expense.objects.all()

	form = ExpenseModelForm()

	if request.method == "POST":
		form = ExpenseModelForm(request.POST)
		if form.is_valid():
			form.save()
		redirect("/expenses")


	return render(request, 'expenses/index.html', {'form':form, 'expenses':expenses})

def update(request, pk):

	data = Expense.objects.get(id = pk)
	form = ExpenseModelForm(instance = data)

	if request.method == "POST":
		form = ExpenseModelForm(request.POST, instance = data)
		if form.is_valid():
			form.save()
			return redirect('/expenses')

	return render(request, 'expenses/update.html', {'form':form})

def delete(request, pk):

	data = Expense.objects.get(id = pk)

	if request.method == "POST":
		data.delete()
		return redirect("/expenses")

	return render(request, 'expenses/delete.html', {'data':data})