from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from.models import User

def index(request):
    context={
        "all_users":User.objects.all()
            }
    return render(request,"index.html",context)


def process(request):
    firstname_from_form = request.POST["fname"]
    lastname_from_form = request.POST["lname"]
    email_from_form = request.POST["email"]
    age_from_form = request.POST["age"]



    new_user=User.objects.create(first_name=firstname_from_form,last_name=lastname_from_form,email=email_from_form,age=age_from_form)
    new_user.save()

    # context={
    #     "fnam":firstname_from_form,
    #     "lname":lastname_from_form,
    #     "email":email_from_form,
    #     "age":age_from_form
    # }
    return redirect("/")