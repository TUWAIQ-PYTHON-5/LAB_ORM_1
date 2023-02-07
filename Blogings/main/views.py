from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
from datetime import date



def leatestBlogs(request : HttpRequest):
    leatestBlogs = Blog.objects.all()
    context = {"leatestBlogs" : leatestBlogs}
    return render(request, "main/leatestBlogs.html", context)


def addBlog(request : HttpRequest):

    if request.method == "POST":
        newBlog = Blog(title= request.POST["title"], content = request.POST["content"], isPublish = request.POST["isPublish"])
        newBlog.save()
        return redirect("main:leatestBlogs")


    return render(request, "main/addBlog.html")

