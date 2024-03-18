from django.shortcuts import render

# Create your views here.



def home_page_user(request):
    return render(request,"home_page_user.html")