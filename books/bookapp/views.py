from django.http import request
from django.shortcuts import render,redirect,HttpResponse
#from.models import Book,Author
from . import models

def index(request):
    context={
        "all_books":models.get_allbooks(),
        "all_authors":models.get_allauthors(),
    }
    return render(request,"index.html",context)

def book(request):
    title=request.POST["title"]
    desc=request.POST["desc"]
    models.creat_book(title,desc)
    return redirect("/")

def index2(request):
    context={
        "all_books":models.get_allbooks(),
        "all_authors":models.get_allauthors(),
    }
    return render(request,"index2.html",context)

def author(request):
    #if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        note=request.POST["note"]
        models.creat_author(fname,lname,note)
        return redirect('/auth')
    # else:
    #      context={
    #     "all_books":models.get_allbooks(),
    #     "all_authors":models.get_allauthors(),
    # }
    # return render(request,"index2.html",context)    
def book_information(request,id):
        request.session["bookid"]=id
        context={
        "bookid":models.book_id(id),
        "authors":models.select_book(id),
        "drop2":models.get_allauthors()
    }
        return render(request,"bookinfo.html",context)

        
def author_information(request,id):
        request.session["authorid"]=id
        context={
        "authid":models.author_id(id),
        "books":models.select_author(id),
        "drop":models.get_allbooks()
    }
        return render(request,"authinfo.html",context)
def drop1(request):
    if request.method=="POST":
        drop=request.POST["books"]
        id=request.session["authorid"]
        models.addbook_author(drop,id)
        return redirect("authors/"+str(id))
        
def drop2(request):
    if request.method=="POST":
        drop2=request.POST["author"]
        id=request.session["bookid"]
        models.addAuthor_book(drop2,id)
        return redirect("books/"+str(id))
        
