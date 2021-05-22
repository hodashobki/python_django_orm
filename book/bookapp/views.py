from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse("Hello world")

# Create your views here.
