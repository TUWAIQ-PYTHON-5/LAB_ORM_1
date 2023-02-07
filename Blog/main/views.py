from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
# Create your views here.

  
def read_blog(request : HttpRequest):

    posts= Blog.objects.all()
    context = {"posts" : posts}
    return render(request, "main/index.html", context)



def add_blog(request : HttpRequest):

    if request.method == "POST":
        #to add a new entry
        new_blog = Blog(title=request.POST["title"],Content=request.POST["Content"],is_published=request.POST["is_published"]) 
        new_blog.save()
        return redirect("main:add_page")

    return render(request ,"main/add_blog.html" ) 