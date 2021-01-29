from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .form import PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="Login")
def post_list(request):
	posts = Post.objects.filter(created_date__lte = timezone.now()).order_by('created_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

# Because the URLconf pass variable pk to the view, we have define the function with the corresponding parameter
def post_detail(request, pk):
	post = get_object_or_404(Post, pk = pk)
	return render(request, 'blog/post_detail.html', {'post':post})
	
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)

		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.modified_date = timezone.now()
			post.save()
			return redirect('post_detail', pk = post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk = pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance = post)

		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.modified_date = timezone.now()
			post.save()
			return redirect('post_detail', pk = post.pk)

	else:
		form = PostForm(instance = post)
	return render(request, 'blog/post_edit.html', {'form' : form})

def post_delete(request, pk):
	post = get_object_or_404(Post, pk = pk)

	if request.method == "POST":
		post.delete()
		return redirect('post_list')
	
	return render(request, 'blog/post_delete.html', {'post':post})