from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.home, name="home page"),
    path("new/posts", views.add_post, name="new post" ),
     path("latest/blogs", views.latest_blog, name="latest blogs" ),
]