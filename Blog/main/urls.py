from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.add_blog, name="add_page"),
    path("read/", views.read_blog, name="read_page"),
]