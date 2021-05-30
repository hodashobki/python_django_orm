from django.db import models
import re
import bcrypt



EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex=re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self,postData):
        errors={}
        if len(postData['fname'])<2:
          errors['fname']="First name must be at least 2 characters"
        if not name_regex.match(postData['fname']):
            errors['fname']="First name must include letters only"

        if len(postData['lname'])<2:
          errors['lname']="last name must be at least 2 characters"
        if not name_regex.match(postData['lname']):
            errors['lname']="last name must include letters only" 

        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="Invalide email address"
        
        if len(postData['email'])<1:  
            errors['email']="Email is required"

        if len(postData['pw'])<1:  
            errors['pw']="Password must be at least 8 characters"
        if postData['pw']!=postData['cpw']:
            errors['cpw']="Passwords not matched"   
        return errors

        

    def  login_validator(self,postData):
        errors2={}
        checkemail=postData['email2']
        user=User.objects.filter(email=checkemail)

        if len(checkemail)<1:
            errors2['email2']="Invalide email or password"
        elif not bcrypt.checkpw(postData['pw2'].encode(),user[0].pw.encode()):
            errors2['pw2']="Invalide email or password"
        return errors2        




class User(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    pw=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # book_uploded
    # liked_book


class BookManager(models.Manager):
    def book_validator(self,postData):
        errors3={}
        if len(postData['title'])<1:
          errors3['title']="Title is required "

        if len(postData['desc'])<1:
          errors3['desc']="Description must be at least 5 character "
        return errors3  


class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    uploaded_by=models.ForeignKey(User,related_name="book_uploded", on_delete = models.CASCADE)
    liked_book=models.ManyToManyField(User,related_name="liked_book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=BookManager()


# def newbook(title,desc,uploadby,liked):
#     newbook=Book.objects.create(title=title,desc=desc, uploded_by=User.objects.get(id=request.session[id]))
   

    



