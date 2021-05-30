from typing import ValuesView
from django.urls import path     
from . import views
urlpatterns = [ 
    path('', views.index),
    path('register',views.register),
    path('success',views.success),
    path('log',views.log),
    path('logout',views.logout),
    path('add-book',views.addbook),
    path('books/<int:bookid>',views.bookshow),
    path('edit-book/<int:bookid>',views.editbook),
    path('delete-book/<int:bookid>',views.delete),
    path('addfavorite/<int:id>/<int:bookid>',views.addfavorite),
    path('unfavorite/<int:id>/<int:bookid>',views.unfavorite),




     ]
