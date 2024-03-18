from django.db import models

# Create your models here.
class Complaintdb(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    email=models.CharField(max_length=50,blank=True,null=True)
    udep=models.CharField(max_length=50,blank=True,null=True)
    uroom=models.CharField(max_length=50,blank=True,null=True)
    subject=models.CharField(max_length=50,blank=True,null=True)
    message=models.CharField(max_length=50,blank=True,null=True)


class Signupdb(models.Model):
    username=models.CharField(max_length=50,blank=True,null=True)
    sdep=models.CharField(max_length=50,blank=True,null=True)
    sroom=models.CharField(max_length=50,blank=True,null=True)
    semail=models.CharField(max_length=50,blank=True,null=True,unique=True)
    pass1=models.CharField(max_length=50,blank=True,null=True)
    pass2=models.CharField(max_length=50,blank=True,null=True)