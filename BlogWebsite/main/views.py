from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.

def add_blog(request : HttpRequest):

    if request.method == "POST":
        #to add a new entry
        new_blog = Blog(title= request.POST["title"], content = request.POST["content"], is_published = request.POST["is_published"], publish_date=request.POST["publish_date"])
        new_blog.save()
        return redirect("main:latest_blogs_page")


    return render(request, "main/add.html")


def latest_blogs(request : HttpRequest):

    latest_blogs = Blog.objects.all()

    context = {"latest_blogs" : latest_blogs}
    return render(request, "main/new.html", context)
