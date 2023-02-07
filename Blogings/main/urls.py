from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("leatestBlogs/", views.leatestBlogs, name="leatestBlogs" ),
    path("", views.addBlog, name="addBlog"),
    
]