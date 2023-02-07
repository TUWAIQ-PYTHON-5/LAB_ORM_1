from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import orm



# Create your views here.

def data_base(request:HttpRequest):
    if request.method== "POST":
        #to add a new entry
        new_game = orm(title= request.POST["title"], description = request.POST["Content"], rating = request.POST["is_published"], release_date=request.POST[ "publish_date"])
        new_game.save()
        return redirect("main:data_base")
    return render(request, "Blog/index.html")

def data_blog(request : HttpRequest):

    blog = orm.objects.all()

    context = {"list_blog" : blog}
    return render(request, "blog/index.html", context)