from django.shortcuts import render,redirect,HttpResponse
from.models import User
from . import models


def index(request):
    return render(request,"index.html")


def reg(request):
    fname=request.POST["fname"]
    lname=request.POST["lname"]
    email=request.POST["email"]
    passe=request.POST["passe"]
    cpass=request.POST["cpass"]
    request.session["username"]=fname
    if request.POST["passe"]!=request.POST['cpass']:
        return redirect("/")
    request.session['email']=request.POST['email']    
    models.creat_user(fname,lname,email,passe)
    return redirect("/success")

def success(request):
    context={
        "email":request.session['email']
    } 
    return render(request,"success.html",context)   

def log(request):
    lemail=request.POST["lemail"]
    lpasse=request.POST["lpass"]
    user=User.objects.filter(email=request.POST['lemail'])
    if user:
        if user[0].password==request.POST["lpass"]:
            request.session["email"]=user[0].email
            return redirect("/success")
        return redirect("/")    
    return redirect("/")

def logout(request):
    del request.session["email"]
    return redirect('/')
    