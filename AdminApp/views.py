from django.shortcuts import render,redirect

from AdminApp.models import Departmentdb,Roomdb,Studentdb
from UserApp.models import Complaintdb


# Create your views here.
def index(request):
    return render(request,"index.html")



def adddepartment(request):
    return render(request,"adddepartment.html")


def savedepartment(request):
    if request.method=='POST':
        dn=request.POST.get('dname')
        dh=request.POST.get('dhead')
        dt=request.POST.get('dtime')
        obj=Departmentdb(dname=dn,dhead=dh,dtime=dt)
        obj.save()
        return redirect(adddepartment)



def displaydepartment(request):
    data=Departmentdb.objects.all()
    return render(request,"displaydepartment.html",{'data':data})


def editdepartment(request, dataid):
    data = Departmentdb.objects.get(id=dataid)
    return render(request, "editdepartment.html", {'data': data})


def updatedepartment(request, dataid):
    if request.method == 'POST':
        dn = request.POST.get('dname')
        dh = request.POST.get('dhead')
        dt = request.POST.get('dtime')
        Departmentdb.objects.filter(id=dataid).update(dname=dn,dhead=dh,dtime=dt)
        return redirect(displaydepartment)


def deletedepartment(request, dataid):
    data = Departmentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydepartment)




def addroom(request):
    return render(request,"addroom.html")


def saveroom(request):
    if request.method=='POST':
        rn=request.POST.get('rname')
        obj=Roomdb(rname=rn)
        obj.save()
        return redirect(addroom)



def displayroom(request):
    data=Roomdb.objects.all()
    return render(request,"displayroom.html",{'data':data})


def editroom(request, dataid):
    data = Roomdb.objects.get(id=dataid)
    return render(request, "editroom.html", {'data': data})


def updateroom(request, dataid):
    if request.method == 'POST':
        rn = request.POST.get('rname')
        Roomdb.objects.filter(id=dataid).update(rname=rn)
        return redirect(displayroom)


def deleteroom(request, dataid):
    data = Roomdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayroom)




def addstudent(request):
    data=Departmentdb.objects.all()
    data1=Roomdb.objects.all()
    return render(request,"addstudent.html",{'data':data,'data1':data1})


def savestudent(request):
    if request.method=='POST':
        sn=request.POST.get('sname')
        ag=request.POST.get('age')
        ge=request.POST.get('gender')
        nu=request.POST.get('number')
        em=request.POST.get('email')
        de=request.POST.get('sdepartment')
        sr=request.POST.get('sroom')
        obj=Studentdb(sname=sn,age=ag,gender=ge,number=nu,email=em,sdepartment=de,sroom=sr)
        obj.save()
        return redirect(addstudent)



def displaystudent(request):
    data=Studentdb.objects.all()
    return render(request,"displaystudent.html",{'data':data})



def editstudent(request, dataid):
    data = Studentdb.objects.get(id=dataid)
    data1=Departmentdb.objects.all()
    data2=Roomdb.objects.all()
    return render(request, "editstudent.html", {'data': data,'data1':data1,'data2':data2})


def updatestudent(request, dataid):
    if request.method == 'POST':
        sn=request.POST.get('sname')
        ag=request.POST.get('age')
        ge=request.POST.get('gender')
        nu=request.POST.get('number')
        em=request.POST.get('email')
        de=request.POST.get('sdepartment')
        sr=request.POST.get('sroom')
        Studentdb.objects.filter(id=dataid).update(sname=sn,age=ag,gender=ge,number=nu,email=em,sdepartment=de,sroom=sr)
        return redirect(displaystudent)


def deletestudent(request, dataid):
    data = Studentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaystudent)

def complaints(request):
    data=Complaintdb.objects.all()
    return render(request,"complaints.html",{'data':data})

def deletecom(request, dataid):
    data = Complaintdb.objects.filter(id=dataid)
    data.delete()
    return redirect(complaints)