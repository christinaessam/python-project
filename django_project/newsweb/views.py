from django.shortcuts import render
from django.http import request,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Post

# imports for login & registration
from newsweb.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

###################start login & registration ################################
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            request.session["user_id"] = user.id
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
    #request.session["user_id"] = user.id //error localuser
    
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user ,
'user_id': request.session.get('user_id')}
    )
###################end   login & registration ################################

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

def sport(request):
	#return HttpResponse("hello")
	obj = Post.objects.filter(post_category=1)
	context = {'post':obj}
	return render(request,'sport.html',context)
	
		

