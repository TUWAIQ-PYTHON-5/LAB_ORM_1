from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from .models import Post




# Create your views here.
def home_page(request):

    return render(request , 'main/home.html', {"Welcom" : "Welcome to our Blog Site"})


def add_new_blog(request : HttpRequest):
    if request.method == "POST":
        new_blog = Post(Title=request.POST["Title"],Content=request.POST["Content"],is_published=request.POST["is_published"],publish_date=request.POST["publish_date"])   
        new_blog.save()
        return redirect("main:home_page")
    return render(request , "main/add_blog.html")  


def show_only_what_is_ready_for_publish(request : HttpRequest):
    ready_blog = Post.objects.filter(is_published = True)
    context = {'ready_blog':ready_blog}
    return render(request , 'main/show_ready_blog.html' , context)       


def show_only_what_is_not_ready_for_publish(request : HttpRequest):
    ready_blog = Post.objects.filter(is_published = False)
    context = {'ready_blog':ready_blog}
    return render(request , 'main/show_ready_blog.html' , context)       