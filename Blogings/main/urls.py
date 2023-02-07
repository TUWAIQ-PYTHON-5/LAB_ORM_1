from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.leatestBlogs, name="leatestBlogs" ),
    path("/add/", views.addBlog, name="addBlog"),
    
]