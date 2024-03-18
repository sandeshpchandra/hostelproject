from django.shortcuts import render,redirect
from UserApp.models import Complaintdb,Signupdb
from AdminApp.models import Departmentdb,Roomdb,Studentdb


# Create your views here.



def home_page_user(request):
    pro=Signupdb.objects.get(semail=request.session['semail'])
    return render(request,"home_page_user.html",{'pro':pro})



def savecomplaint(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        ud=request.POST.get('udep')
        ur=request.POST.get('uroom')
        su=request.POST.get('subject')
        ms=request.POST.get('message')
        obj=Complaintdb(name=na,email=em,udep=ud,uroom=ur,subject=su,message=ms)
        obj.save()
        return redirect(home_page_user)



def signinup(request):
    data=Departmentdb.objects.all()
    return render(request,"signinup.html",{'data':data})



def savesignup(request):
    if request.method=="POST":
        na=request.POST.get('username')
        em=request.POST.get('sdep')
        ud=request.POST.get('sroom')
        ur=request.POST.get('semail')
        su=request.POST.get('pass1')
        ms=request.POST.get('pass2')
        obj=Signupdb(username=na,sdep=em,sroom=ud,semail=ur,pass1=su,pass2=ms)
        obj.save()
        return redirect(signinup)

def userlogin(request):
    if request.method=='POST':
        na=request.POST.get('username')
        pwd=request.POST.get('password')
        if Signupdb.objects.filter(semail=na,pass1=pwd).exists():
            request.session['semail']=na
            request.session['pass1']=pwd
            return redirect(home_page_user)
        else:
            return redirect(signinup)
    else:
        return redirect(signinup)


def userlogout(request):
    del request.session['uemail']
    del request.session['upass']
    return redirect(signinup)
