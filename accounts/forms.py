from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class RegisterForm(UserCreationForm):

	username = forms.CharField(
		label = "帳號",
		widget = forms.TextInput(attrs = {'class':'form-control'})
		)
	email = forms.EmailField(
		label = "電子郵件",
		widget = forms.EmailInput(attrs = {'class':'form-control'})
		)
	password1 = forms.CharField(
		label = "密碼",
		widget = forms.PasswordInput(attrs = {'class':'form-control'})
		)
	password2 = forms.CharField(
		label = "確認密碼",
		widget = forms.PasswordInput(attrs = {'class':'form-control'})
		)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
	username = forms.CharField(
		label = "帳號",
		widget = forms.TextInput(attrs = {'class':'form-control'})
		)

	password = forms.CharField(
		label = "密碼",
		widget = forms.PasswordInput(attrs = {'class':'form-control'})
		)

class CustomerModelForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = "__all__"
		widgets = {
			'name':forms.TextInput(attrs = {'class':'form-control', 'style': 'width:50%;'}),
			'email':forms.TextInput(attrs = {'class':'form-control', 'style': 'width:50%;'}),
			'tel':forms.TextInput(attrs = {'class':'form-control', 'style': 'width:50%;'})
			}
		labels = {
			'name':'姓名',
			'email':'信箱',
			'tel':'電話'
		}

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		if email.endswith('@hotmail.com'):
			raise forms.ValidationError("不可以用 hotmail 電子郵件")

		return email