from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import SpaceObject
from .forms import PostForm
from datetime import datetime
# Create your views here.

def post_home(request):
	home = "Это страница хоме"
	return render_to_response('home.html',{'name':home})

def post_detail(request,id=None):
	instance = get_object_or_404(SpaceObject,id=id)
	context={'title':'Post details','instance':instance}
	return render(request,"post_detail.html",context)

def post_update(request):
	return HttpResponse('<h1>update</h1>')

def post_delete(request):
	return HttpResponse('<h1>delete</h1>')

def post_list(request):
	queryset = SpaceObject.objects.all()
	context={'queryset':queryset, 'title':'Post List'}
	return render(request,'index.html',context)

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context={
		'form' : form
	}
	return render(request,'post_create.html',context)

def post_update(request,id=None):
	instance = get_object_or_404(SpaceObject,id=id)
	form = PostForm(request.POST or None,instance= instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		'title': instance.name,
		'instance': instance,
		'form': form
	}
	return render(request,'post_create.html',context)