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
    user=User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],email=request.POST['email'],pw=pw_hash)
    request.session['id']=user[0].id
    # x=new_user.id
    # print(x)
    request.session['fname']=request.POST["fname"]
    # last_user=User.objects.last()
    # id=last_user.id
    return redirect("/success")
    



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
            request.session['id'] = loged_user.id
            request.session['fname'] = loged_user.fname

        return redirect("/success")  
    return  redirect("/") 

def success(request):
    #if 'id' not in request.session:
         #loged_user=User.objects.get(id=request.session['id'])
    context={
            "fname":request.session["fname"],
            #"user":User.objects.get(id=request.session['id']),
            "messages":Message.objects.all(),
            "comments":Comment.objects.all()

        }
    return render(request,"wall.html",context) 
    
                              

def message(request):
    new_message=Message.objects.create(user=User.objects.get(id=request.session['id']),content=request.POST["message"])
    return redirect('/success')

def comment(request):
    new_comment=Comment.objects.create(message=Message.objects.get(id=request.POST["messagid"]),user=User.objects.get(id=request.session['id']),content=request.POST["content"])
    

    return redirect('/success')

def logout(request):
    #del request.session['id']
    return redirect('/')    


