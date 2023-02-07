from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("add/", views.addBlog, name="addBlog"),
    path("latest/", views.latestBlogs, name="latestBlogs" )
]