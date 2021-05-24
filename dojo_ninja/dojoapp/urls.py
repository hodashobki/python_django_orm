from django.urls import path
from . import views

urlpatterns=[
     path("",views.index),
     path("proccess",views.proc1),
     path("proccess1",views.proc2),
 ]