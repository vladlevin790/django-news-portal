from django.urls import path
from django.contrib.auth import views as auth_views
from website.views import *

urlpatterns = [
    path('',index,name='home'),
    path('category/<int:id>', index),
    path('news/<int:id>', news_page),
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
]
