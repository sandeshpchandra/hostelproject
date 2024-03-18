from django.db import models

# Create your models here.
class Departmentdb(models.Model):
    dname=models.CharField(max_length=50,blank=True,null=True)
    dhead=models.CharField(max_length=50,blank=True,null=True)
    dtime=models.CharField(max_length=50,blank=True,null=True)


class Roomdb(models.Model):
    rname=models.CharField(max_length=50,blank=True,null=True)


class Studentdb(models.Model):
    sname=models.CharField(max_length=50,blank=True,null=True)
    age=models.CharField(max_length=50,blank=True,null=True)
    gender=models.CharField(max_length=50,blank=True,null=True)
    number=models.CharField(max_length=50,blank=True,null=True)
    email=models.CharField(max_length=50,blank=True,null=True)
    sdepartment=models.CharField(max_length=50,blank=True,null=True)
    sroom=models.CharField(max_length=50,blank=True,null=True)
