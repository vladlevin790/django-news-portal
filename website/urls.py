from django.urls import path
from website.views import *

urlpatterns = [
    path('',index),
    path('category/<int:id>', index),
]
