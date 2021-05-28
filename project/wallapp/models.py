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

class Message(models.Model):
    user=models.ForeignKey(User,related_name="message",on_delete = models.CASCADE)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message=models.ForeignKey(Message,related_name='comments',on_delete = models.CASCADE) 
    user=models.ForeignKey(User,related_name='comments',on_delete = models.CASCADE)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


   

    



