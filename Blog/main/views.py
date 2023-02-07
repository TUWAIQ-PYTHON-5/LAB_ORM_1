from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
# Create your views here.
def add_blog(request : HttpRequest):

    if request.method == "POST":
        #to add a new entry
        new_blog = Blog(Title=request.POST["Title"],Content=request.POST["Content"],is_published=request.POST["is_published"],publish_date=request.POST["publish_date"]) 
        new_blog.save()
        return redirect("main:add_page")

    return render(request ,"main/add_blog.html") 
  



def read_blog(request : HttpRequest):

    read_blog = Blog.objects.all()

    context = {"read_blog" : read_blog}
    return render(request, "main/read_blog.html", context)
