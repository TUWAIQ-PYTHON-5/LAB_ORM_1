from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog

posts = [
    { 'title': 'the first post',
    'content': 'tester',
    'is_published': '',
    'publish_date': '7-2-2023',
    }
]

def home(request):
    context = {
        'title' : 'home page',
        'posts' : posts,

    }
    return render(request, 'Blog/index.html', context )


def about(request):

     return render(request, 'Blog/about.html', {'title': 'who am i'})
    



def add_Blog(request : HttpRequest):

    if request.method == "POST":
        #to add a new entry
        new_blog = Blog(title= request.POST["title"], description = request.POST["description"], rating = request.POST["rating"], release_date=request.POST["release_date"])
        new_blog.save()
        return redirect("games:latest_games_page")


    return render(request, "games/add_Blog.html")


def latest_Blog(request : HttpRequest):

    latest_games = Game.objects.all()

    context = {"latest_games" : latest_games}
    return render(request, "games/index.html", context)

