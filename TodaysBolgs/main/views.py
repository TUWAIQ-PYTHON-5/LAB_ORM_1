from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.

def main_page(request : HttpRequest):
    
    return render(request, 'main/main.html')