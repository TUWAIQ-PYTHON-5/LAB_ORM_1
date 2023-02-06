from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpRequest
from .models import Subject


def home_page(request : HttpRequest):
    return render(request,"subjects/home_page.html")


def write_page(request : HttpRequest):

    if request.method == "POST":
        new_subject = Subject(title= request.POST["title"], content = request.POST["content"], is_published = request.POST["is_published"], published_date=request.POST["published_date"])
        new_subject.save()
        return redirect("subjects:read_page")

    return render(request,"subjects/write.html")
    

def read_page(request :HttpRequest):
    
    subjects_save = Subject.objects.all()
    context = {"subjects_save" : subjects_save}
    return render(request,"subjects/read.html", context)
    

def about_page(request : HttpRequest):
    return render(request,"subjects/about.html")


