from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from datetime import datetime
# Create your views here.

def post_home(request):
	home = "Это страница хоме"
	return render_to_response('home.html',{'name':home})

def post_detail(request,id=None):
	instance = get_object_or_404(Post,id=id)
	context={'title':'Post details','instance':instance}
	return render(request,"post_detail.html",context)

def post_update(request):
	return HttpResponse('<h1>update</h1>')

def post_delete(request):
	return HttpResponse('<h1>delete</h1>')

def post_list(request):
	queryset = Post.objects.all()
	context={'queryset':queryset, 'title':'Post List'}
	return render(request,'index.html',context)

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	#if request.method == 'POST':
	#	title = request.POST.get('title')
	#	content = request.POST.get('content')
	# 	#author = request.POST.get('post_author')
	#	Post.objects.create(title=title,content=content,timestamp=datetime.now(),updated=datetime.now())
	context={
		'form' : form
	}
	return render(request,'post_create.html',context)

def post_update(request,id=None):
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		'title': instance.title,
		'instance': instance,
		'form': form
	}
	return render(request,'post_create.html',context)