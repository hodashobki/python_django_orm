from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('show/new',views.show_new),
    path('process',views.process),
    path('processedit/show/<int:id>',views.processedit),
    path('show/<int:show_id>',views.success),
    path('show/edit/<int:id>',views.edit),
    path('show/<int:show_id>/destroy',views.destroy)
    
]

