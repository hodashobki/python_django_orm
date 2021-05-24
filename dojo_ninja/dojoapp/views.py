from django.shortcuts import render,redirect,HttpResponse
from.models import Dojo,Ninja
from . import models

def index(request):
    context = {
        "alldojo": Dojo.objects.all()
    }
    return render(request,"index.html",context)



def proc1(request):
    name=request.POST["name"]
    city=request.POST["city"]
    state=request.POST["state"]
    models.creat_dojo(name,city, state)
    return redirect("/")


def proc2(request):
    fname=request.POST["fname"]
    lname=request.POST["lname"]
    dojo=request.POST["dojo"]
    models.creat_ninja(dojo,fname,lname)
    return redirect("/")    