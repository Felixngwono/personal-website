from django.contrib.admin.templatetags.admin_modify import register
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from urllib3 import request

from StoryTeller.models import BlogPost, PortfolioItem, User
from .forms import BlogPostForm, MyUserCreationForm, PortfolioForm, ContactusForm, eventsForm


# Create your views here.

def me(request):
    
    return render(request,'home.html')

def index(request):
    form=MyUserCreationForm()
    if request.method=='POST':
        form=MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    context= {'form':form}
    return render(request,'index.html',context)

def signup(request):
    return render(request,'signup.html')



def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse('User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.info(request,'Login successful')
            return redirect('index')
        else:
             messages.warning(request,'Wrong username or password')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    messages.info(request,"Its sad to see you leave, welcome again")
    return redirect('login') 


def signup(request):
    form =MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
                user = form.save(commit=False)
                user.email = user.email
                user.save()
                messages.info(request,'Registration successful, login to continue to main page')
                return redirect('login')
        else:
            messages.warning(request,'An error occured during registration')

    return render(request, 'signup.html', {'form': form})

def blog(request):
    
    form=BlogPostForm()
    if request.method=="POST":
        form=BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={ 'form':form}
    return render(request, 'blogpost.html', context)

def Portfolio(request):
    blog_posts=PortfolioItem.objects.all()
    form=PortfolioForm()
    if request.method=="POST":
        form=PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={ 'form':form}
    return render(request, 'portfoliopost.html', context)


def ContactusPage(request):
    form = ContactusForm()
    
    if request.method == 'POST':
            form = ContactusForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')     
    context={'form':form}
    return render(request, 'contact_us.html',context)


def events(request):
    form= eventsForm()
    if request.method=='POST':
        form=eventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={'form':form}
    return render(request, 'events.html',context)

def about(request):
    return render(request,'about.html')