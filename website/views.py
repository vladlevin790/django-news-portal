from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import *
from .forms import *

def index(request, id=None):
    data = {
        "categories": Categories.objects.all(),
        "news" : News.objects.all()
    }
    if id:
        data["category"] = Categories.objects.get(id=id)
        data["news"] = News.objects.filter(category=id)
    return render(request, "index.html",data)

def news_page(request, id):
    data = {
        "news" : News.objects.get(id=id),
        "review_form": ReviewForm(),
        "reviews": Reviews.objects.filter(news=id)
    }
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.news = News.objects.get(id=id)
            review.save()

    return render(request, "news_page.html",data)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

