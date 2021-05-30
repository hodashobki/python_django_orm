from django.shortcuts import render,redirect
from .models import User
from .models import Book
from .models import BookManager
from .models import UserManager
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
    #if pas==conf
    pw_hash=bcrypt.hashpw(request.POST['pw'].encode(),bcrypt.gensalt()).decode()
    user=User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],email=request.POST['email'],pw=pw_hash)
    request.session['id']=user.id
    # x=new_user.id
    # print(x)
    request.session['fname']=request.POST["fname"]
    return redirect("/success")

def success(request):
    context={
        "fname":request.session["fname"],
        "loged_user":User.objects.get(id=request.session['id']),
        "books":Book.objects.all(),
        'users':User.objects.all()
    }
    return render(request,"book.html",context) 

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
            #lastuser=User.objects.last()
            #request.session['id']=lastuser.id

        return redirect("/success")  
    return  redirect("/")                        

################################

def addbook(request):
    errors3=Book.objects.book_validator(request.POST)
    if len(errors3)>0:
        for key, value in errors3.items():
            messages.error(request,value)
        return redirect("/success")
    
    title=request.POST['title']
    desc=request.POST['desc']

    uploaded_by_id = request.session['id']
    uploaded_by = User.objects.get(id=uploaded_by_id)
    

    book=Book.objects.create(title=title,desc=desc,uploaded_by=uploaded_by)
    
    request.session['bookid']=book.id
    #last=Book.objects.last()
    #request.session['bookid']=last.id

    # book=Book.objects.create(title=title,desc=desc
    # ,uploaded_by=User.objects.get(id=request.session[id])) 
    return redirect("/success") 


def bookshow(request,bookid):
    #uploaded_by_id = request.session['id']
    this_book=Book.objects.get(id=bookid)
    book_uploder=this_book.uploaded_by_id
    if request.session['id']==book_uploder:
        context = {
            'book': this_book,
            'users': this_book.liked_book.all(),
            "loged_user":User.objects.get(id=request.session['id']),
        }
        return render(request,'edit.html', context)
    else:
        # context = {
        #     'book':  this_book,
        #     'users': this_book.liked_book.all(), 
        # }
        # return render(request,'book.html',context) 
        return redirect('/success')   

def editbook(request,bookid):
    c=Book.objects.get(id=bookid)
    c.desc=request.POST['desc2'] 
    c.save()
    return redirect('/books/'+str(bookid))     

def delete(request,bookid):
    this_book=Book.objects.get(id=bookid)
    book_uplodedby=this_book.uploaded_by_id
    if request.session["id"]==book_uplodedby:
        this_book.delete()
        return redirect('/success')

    else:
        return redirect('/')

def addfavorite(request,id,bookid):
    c=User.objects.get(id=id)
    b=Book.objects.get(id=bookid)
    c.liked_book.add(b)

    # context = {
    #         'book':Book.objects.all(),
    #         'users':User.objects.all(), 
    #     }
    this_book=Book.objects.get(id=bookid)
    book_uploder=this_book.uploaded_by_id

    context = {
            'book': this_book,
            'users': this_book.liked_book.all(),
            "loged_user":User.objects.get(id=request.session['id']),
        }
    return render(request,"addfavorite.html",context)

def unfavorite(request,id,bookid):
    this_book=Book.objects.get(id=bookid)
    this_user=User.objects.get(id=id)
    this_book.liked_book.remove(this_user)
    return redirect('/success')

def logout(request):
    return redirect('/')
