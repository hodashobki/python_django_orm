from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('book',views.book),
    path('auth',views.index2),
    path('author',views.author),
    path('books/<int:id>',views.book_information),
    path('authors/<int:id>',views.author_information),
    path('drop1',views.drop1),
    path('drop2',views.drop2),

    ]