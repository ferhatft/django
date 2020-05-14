from django.shortcuts import render,redirect
from .forms import RegisterForm,loginForm

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username= username)
        newUser.set_password(password)
        
        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla Kayıt oldunuz")

        return redirect("index")
    context = {
        "form": form

    }

    return render(request,"register.html",context)

def loginUser(request):
    form = loginForm(request.POST or None)
    context = {
        "form": form    
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username= username,password = password)
        if user is None:
            messages.info(request,"Yanlış kullanıcı adı veya parola")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla giriş yapıldı")
        login(request,user)
    
        return redirect("index")
    
    
    return render(request,"login.html",context)
    
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı")
    return redirect("index")