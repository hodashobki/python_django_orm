from django.shortcuts import render, redirect, HttpResponse
from.models import Author,Book

def index(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request,"index.html",context)


