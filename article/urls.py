from django.contrib import admin
from django.urls import path

app_name ="article"

from . import  views
urlpatterns = [
    path('dashboard/',views.dashboard, name= "dashboard"),
    path('addarticle/',views.addarticle, name= "addarticle"),
    path('article/<int:id>',views.detail, name= "detail"),
    path('update/<int:id>',views.update, name= "update"),
    path('delete/<int:id>',views.delete, name= "delete"),
    path('',views.articles, name= "articles"),
    path('comment/<int:id>',views.addComment, name= "addComment"),
    
]