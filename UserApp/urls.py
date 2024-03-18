from django.urls import path

from AdminApp import views
from UserApp import  views

urlpatterns = [
    path('home_page_user/',views.home_page_user,name="home_page_user"),
]