from django.db import models

class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    desc=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    dojo=models.ForeignKey(Dojo, related_name="ninjas",on_delete = models.CASCADE) 
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
 
def creat_dojo(name,city,state):
    new_dojo=Dojo.objects.create(name=name,city=city,state=state)

def creat_ninja(dojo,fname,lname):
    new_ninja=Ninja.objects.create(dojo=Dojo.objects.get(name=dojo),first_name=fname,last_name=lname)