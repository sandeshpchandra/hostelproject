from django.urls import path

from AdminApp import views
from UserApp import  views

urlpatterns = [
    path('home_page_user/',views.home_page_user,name="home_page_user"),
    path('savecomplaint/',views.savecomplaint,name="savecomplaint"),
    path('signinup/',views.signinup,name="signinup"),
    path('savesignup/',views.savesignup,name="savesignup"),
    path('userlogin/',views.userlogin,name="userlogin"),
]