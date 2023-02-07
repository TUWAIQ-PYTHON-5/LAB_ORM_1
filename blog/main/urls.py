from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('' , views.home_page , name='home_page'),
    path('add/' , views.add_new_blog , name='add_blog'),
    path('ready_to_share/', views.show_only_what_is_ready_for_publish , name='ready_share'),
    path('not_ready_to_share/', views.show_only_what_is_not_ready_for_publish , name='not_ready_share'),
    path('show_all' , views.show_all , name='show_all')
    
]