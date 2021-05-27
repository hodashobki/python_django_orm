from semiapp import models
from django.shortcuts import render,redirect,HttpResponse
from .  import models

from django.contrib import messages
   
from .models import Show


#################################
def index(request):
    context={
       "allshow": models.all_shows(),
    }
    return render(request,"main.html",context)


def show_new(request):
    return render(request,'form.html')

def process(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:    
        title=request.POST["title"]
        network=request.POST["network"]
        redate=request.POST["redate"]
        desc=request.POST["desc"]
        models.new_show(title,network,redate,desc)
        last_show=models.Show.objects.last()
        id=last_show.id
        return redirect('/show/'+str(id)) 
     

def success(request,show_id):
    context={
        "showid":models.show_by_id(show_id)
    }
    return render(request,"tv_show.html",context)


def edit(request,id):
    context={
        "showid":models.show_by_id(id)
    }
    return render(request,"edit.html",context) 
    
       
def processedit(request,id):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        show_id= models.Show.objects.get(id = id)
        show_id.title = request.POST['title']
        show_id.network = request.POST['network']
        show_id.release_date = request.POST['redate']
        show_id.description = request.POST['desc']
        show_id.save()
        return redirect('/show/'+str(id))    

   
def destroy(request,show_id):
    show =models.show_by_id(show_id) 
    show.delete()
    return redirect('/')

       