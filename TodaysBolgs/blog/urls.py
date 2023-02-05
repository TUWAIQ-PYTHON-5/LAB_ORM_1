from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("add/", views.add_blog, name="add_new_blog"),
    path("view/", views.view_blogs, name="view_blogs_page" )
    
]