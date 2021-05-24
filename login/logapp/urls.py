from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('process',views.reg),
    path('success',views.success),
    path('logout',views.logout),
    path('process2',views.log),
]
