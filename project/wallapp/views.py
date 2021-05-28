from django.shortcuts import render,redirect
from .models import User,Message,Comment
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,"reg.html")

def register(request):
    errors=User.objects.register_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/")
    
    pw_hash=bcrypt.hashpw(request.POST['pw'].encode(),bcrypt.gensalt()).decode()
    new_user=User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],email=request.POST['email'],pw=pw_hash)
    request.session['id']=new_user.id
    # x=new_user.id
    # print(x)
    request.session['fname']=request.POST["fname"]
    return redirect("/success")

def success(request):
    context={
        "fname":request.session["fname"],
        "loged_user":User.objects.get(id=request.session['id'])

    }
    return render(request,"wall.html",context) 

def log(request):
    errors2=User.objects.login_validator(request.POST)
    if  len(errors2)>0:
        for key, value in errors2.items():
            messages.error(request,value)
        return redirect("/")
    user=User.objects.filter(email=request.POST['email2'])
    if user:
        loged_user=user[0]
        if bcrypt.checkpw(request.POST['pw2'].encode(), loged_user.pw.encode()):
            request.session['userid'] = loged_user.id
            request.session['fname'] = loged_user.fname

        return redirect("/success")  
    return  redirect("/")                        
    
