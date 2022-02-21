
from .models import Task
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.db.models import Q

@login_required(login_url="login")
def home(request):
    q= request.GET.get("q")
    if q == None:
        q=""
    
    task_search=Task.objects.filter(
        Q(body__icontains=q)
    )
    tasks=Task.objects.all()
    if request.method == "POST":
        task=Task.objects.create(
            body=request.POST.get("body"),
            user=request.user
        )
        task.save()
        return redirect("home")

    context={"task_search":task_search}
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

@login_required(login_url="login")
def update_task(request,pk):
    task=Task.objects.get(id=pk)
    forms=TaskForm(instance=task)

    if request.method=="POST":
        forms=TaskForm(request.POST,instance=task)
        if forms.is_valid():
            forms.save()
            return redirect("home")
    context={"forms":forms}
    return render(request,"to_do_app/update_tasks.html",context)

@login_required(login_url="login")
def delete_task(request,pk):
    task=Task.objects.get(id=pk)

    if request.method=="POST":
        task.delete()
        return redirect("home")
    context={"obj":task}
    return render(request,"to_do_app/delete_page.html",context)

@login_required(login_url="login")
def statement(request,pk):
    task=Task.objects.filter(id=pk).values("statement")

    for i in task:
        if i=={"statement":True}:
            i=Task.objects.filter(id=pk).values("statement").update(statement=False)
        else:
            i=Task.objects.filter(id=pk).values("statement").update(statement=True)
    
    
    return redirect("home")


#spraviť prečiarknutie tasku