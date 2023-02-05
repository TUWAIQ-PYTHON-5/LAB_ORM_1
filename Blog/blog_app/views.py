from django.shortcuts import render , redirect
from django.http import HttpRequest ,HttpResponse
from .models import Posts

# Create your views here.




def index(request : HttpRequest):

    blogs = Posts.objects.all()
    context = {
        "blog" : blogs
    }


    return render(request ,"blogs/index.html" , context)




def add_post(request : HttpRequest):

    if request.method == "POST":
        #to add a new entry
        
        new_post = Posts(
            
            title = request.POST["title"],
            content = request.POST["content"],
            is_published = request.POST.get('is_published',False),
            publish_date = request.POST["publish_date"]
        ) 
        new_post.save()
        return redirect("blog:blogs_page")


    return render(request, "blogs/Add_post.html")

