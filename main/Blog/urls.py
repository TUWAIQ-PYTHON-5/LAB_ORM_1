from django.urls import path
from . import views

app_name = "Blog"

urlpatterns = [
    path("", views.home, name= "home"),
    path('about/', views.about, name="about"),
    path("add/", views.add_Blog, name="add_new_blog"),
    path("latest/", views.latest_Blog, name="latest_blog_page"),

]