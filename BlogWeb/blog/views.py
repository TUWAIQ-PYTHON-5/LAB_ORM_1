from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.

def home(request):
    return render(request,'blog/home.html')




def add_post(request : HttpRequest):

    if request.method == "POST":

        new_post = Post(Title= request.POST["Title"], Content = request.POST["Content"], is_published = request.POST["is_published"],publish_date = request.POST["publish_date"])
        new_post.save()
        return redirect("blog:latest blogs")
    
    
    return render(request, "blog/add_new.html")
    


def latest_blog(request : HttpRequest):

    latest_blog = Post.objects.all()

    context = {"latest_blog" : latest_blog}
    return render(request, "blog/blogs.html", context)
