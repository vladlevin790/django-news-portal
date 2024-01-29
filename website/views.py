from django.shortcuts import render
from .models import *

def index(request):
    data = {
        "categories": Categories.objects.all(),
        "news":News.objects.all()
    }
    return render(request, "index.html",data)
    