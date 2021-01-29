from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post

def index(request):
	posts = Post.objects.all()
	return render(request, 'posts/index.html', {'posts':posts})