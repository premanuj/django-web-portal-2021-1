from django.http import HttpResponse
from django.shortcuts import render

def home_backup(request):
    return HttpResponse("I am home page")

def index(request):
    template_name = 'index.html'
    context = {"grettings": "Hello world from home"}
    return render(request, template_name, context)

def home(request):
    template_name = 'home.html'
    context = {"grettings": "Hello world from home"}
    return render(request, template_name, context)