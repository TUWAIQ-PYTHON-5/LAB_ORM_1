from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.


def home_page (request : HttpRequest):
    Posts = Post.objects.all()
    context = {"posts" : Posts}
    if request.method == "POST":
        new_post = Post(title=request.POST["title"], Content=request.POST["content"], is_published=request.POST["is_published"])
        new_post.save()
        return redirect("main:home_page")
    return render (request,"main/home.html", context)




