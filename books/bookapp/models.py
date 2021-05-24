from django.db import models
from . import views
class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    books=models.ManyToManyField(Book,related_name='authors')
    notes=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)    


def creat_book(title,desc):
    new_book=Book.objects.create(title=title,desc=desc)

def get_allbooks():
    return Book.objects.all()       

def creat_author(fname,lname,note):
    new_author=Author.objects.create(first_name=fname,last_name=lname,notes=note)
    

def get_allauthors():
    return Author.objects.all() 

def book_id(id):
    return Book.objects.get(id=id)           

def author_id(id):
    return Author.objects.get(id=id)

def select_book(id):
    bbook=Book.objects.get(id=id)
    return bbook.authors.all()

def select_author(id):
    aauthor=Author.objects.get(id=id)
    return aauthor.books.all()    

def addbook_author(title,id):
    book=Book.objects.get(title=title)
    author=Author.objects.get(id=id)
    return author.books.add(book)

def addAuthor_book(fname,id):
    author=Author.objects.get(first_name=fname)
    book1=Book.objects.get(id=id)
    return book1.authors.add(author)