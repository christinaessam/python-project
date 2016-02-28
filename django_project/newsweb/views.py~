from django.shortcuts import render
from django.http import request,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from models import Post


# Create your views here.
def showpost(request):
	#return HttpResponse("hello")
	obj = Post.objects.get(id = 1)
	context = {'post':obj}
	return render(request,'ok.html',context)
	
def index(request):
	blogs = Post.objects.all()
		
	if request.method == "POST":
		usname = request.POST['username']
		pswd = request.POST['password']
		user = authenticate(username=usname , password=pswd)
		if user is not None:
			login(request,user)
			return render(request,'blog.html',{'testvar':"Testing 2",'blogs':blogs,'user':user})		
	return render(request,'blog.html',{'testvar':"Testing 2",'blogs':blogs,'user':None})

#create post <in admin page>
def createpost(requset):
	newpost=Post()
	newpost.title = request.POST['title']
	newpost.post_content = request.POST['post_content']
	newpost.author = request.user
	newpost.post_category_id = request.POST['category']
	newpost.save()
	return render(request,'blog.html',{'testvar':"Testing 2",'blogs':blogs,'user':user}) 
	
		

