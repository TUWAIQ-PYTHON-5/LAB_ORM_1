from django.urls import path
from . import views

app_name = 'subjects'

urlpatterns = [
    
    path('',views.home_page , name="home_page"),
    path('read/',views.read_page,name="read_page"),
    path('write/',views.write_page,name="write_page"),
    path('about/',views.about_page,name="about_page"),

]