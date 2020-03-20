from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Post


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