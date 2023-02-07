from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
from datetime import date



def addBlog(request : HttpRequest):

    if request.method == "POST":
        today = date.today()
        newBlog = Blog(title= request.POST["title"], description = request.POST["content"], isPublish = request.POST["isPublish"], writingDate=request.POST[today])
        newBlog.save()
        return redirect("main:leatestBlogs")


    return render(request, "main/addBlog.html")


def leatestBlogs(request : HttpRequest):
    latest_games = Blog.objects.all()
    context = {"leatestBlogs" : leatestBlogs}
    return render(request, "main/leatestBlogs.html", context)