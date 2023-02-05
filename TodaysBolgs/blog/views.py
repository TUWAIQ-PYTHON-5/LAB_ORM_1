from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.

def blog_page(request : HttpRequest):
    
    return render(request, 'blog/blog.html')

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog
# Create your views here.


def add_blog(request : HttpRequest):

    if request.method == "POST":
        #to add a new entry
        new_blog = Blog(title= request.POST["title"], Content = request.POST["Content"], is_published = request.POST["is_published"], publish_date=request.POST["publish_date"])
        new_blog.save()
        return redirect("blogs:view_blogs_page")


    return render(request, "blogs/add_blog.html")


def view_blogs(request : HttpRequest):

    view_blogs = Blog.objects.all()

    context = {"view_blogs" : view_blogs}
    return render(request, "blogs/index.html", context)