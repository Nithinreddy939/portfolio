from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from .models import portfolio_members

# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='signin')
def projects(request):
    return render(request, 'projects.html')
@login_required(login_url='signin')
def certifications(request):
    return render(request, 'certifications.html')
@login_required(login_url='signin')
def about(request):
    return render(request, 'about.html')

def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('signin')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        user = auth.models.User.objects.create_user(username=username, password=password, email=email)
        user.save()
        if user:
            auth.login(request,user)
            return redirect('signin')
        else:
            return redirect('signup')

    return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
