from .models import Task
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def home(request):
    tasks=Task.objects.all()
    if request.method == "POST":
        task=Task.objects.create(
            body=request.POST.get("body")
        )
        task.save()
        return redirect("home")

    context={"tasks":tasks}
    return render(request,"to_do_app/home.html",context)

def register_page(request):
    form =UserCreationForm()

    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"Error during registration process")

    context={"form":form}
    return render(request,"to_do_app/login_register.html",context)

def login_page(request):
    page= "login"
    if request.method == "POST":
        username=request.POST.get("username").lower()
        password=request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home") 
        else:
            messages.error(request,"Username or Password does not exist")
    context={"page":page}
    return render(request,"to_do_app/login_register.html",context)


def logout_user(request):
    logout(request)
    return redirect("home")