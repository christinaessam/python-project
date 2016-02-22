from django.shortcuts import render
from django.http import HttpResponse
from models import Post

# Create your views here.

def index(request):
	#return HttpResponse("hello")
	obj = Post.objects.get(id = 1)
	context = {'post':obj}
	return render(request,'ok.html',context)
