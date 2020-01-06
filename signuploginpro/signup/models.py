from django.db import models

class SignupData(models.Model):
    firstname = models.CharField(max_length=100,null=True,blank=True)
    lastname = models.CharField(max_length=20,null=True,blank=True)
    username = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password1 = models.CharField(max_length=20,null=True,blank=True)
    password2 = models.CharField(max_length=20,null=True,blank=True)
    mobile = models.BigIntegerField()

