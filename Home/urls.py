from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
   path('', views.index, name="index"),
   path('post', views.post, name="post"),
   path('blog', views.blog, name="blog"),
]
