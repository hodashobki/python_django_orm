from django.db import models
from datetime import date

#from . import views

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        today=date.today()
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) ==0:
            errors["title"] = "Title Field is required"
        elif len(postData['title']) < 2:
            errors["title"] = "Title name should be at least 2 characters"
        if len(postData['network']) ==0:
            errors["network"] = "Network Field is required"    
        elif len(postData['network']) < 3:
            errors["network"] = "Network  should be at least 2 characters"
        if len(postData['desc']) == 0:
            errors["desc"] = "Description is required"    
        elif len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        if len(postData['redate']) == 10:
            errors["redate"] = "Description is required"    
        # elif len(postData['redate']) >str(today):
        #     errors["redate"] = "That's in the future ?"
                
        return errors

class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    released_date=models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()


def new_show(title,network,redate,desc):
    newshow=Show.objects.create(title=title,network=network,released_date=redate,description=desc)
    return newshow

def all_shows():
    return Show.objects.all()

def show_by_id(id):
    showid=Show.objects.get(id=id)
    return showid


