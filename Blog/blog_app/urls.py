from django.urls import path
from . import views





app_name = "blog"

urlpatterns = [
    path("", views.index, name="blogs_page" ),
    path("blogs/add/", views.add_post, name="add_new_post"),
]
