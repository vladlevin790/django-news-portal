from django.shortcuts import render
from .models import *

def index(request, id=None):
    data = {
        "categories": Categories.objects.all(),
        "news" : News.objects.all()
    }
    if id:
        data["news"] = News.objects.filter(category=id)
    return render(request, "index.html",data)

def news_page(request, id):
    data = {
        "news" : News.objects.get(id=id)
    }
    return render(request, "news_page.html",data)
    