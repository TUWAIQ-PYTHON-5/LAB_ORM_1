from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
   path("", views.latest_blogs, name="latest_blogs_page" ),
   path("add/", views.add_blog, name="add_new_blog")
  
    
]