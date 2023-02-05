from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Blog


def add_blog(request:HttpRequest):
    if request.method == "POST":
       new_blog=Blog(Title=request.POST["Title"],Content=request.POST["Content"],is_published = request.POST.get('is_published', False),publish_date=request.POST["publish_date"])
       new_blog.save()
       return redirect('blog:read_blog')

    return render(request, "blog/add_blog.html")

def read_blog(request:HttpRequest):
    read_blog = Blog.objects.all()

    context = {"read_blog" :read_blog}
    return render(request, "blog/index.html", context)


