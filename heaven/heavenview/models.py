from django.contrib.auth.models import User
from django.db import models
from django.contrib import messages
from django.core import validators
from django.core.validators import *
from django import forms


class Contact(models.Model):
    name=models.CharField(max_length=250, null=True)
    email=models.EmailField(max_length=200,null=True)
    messages=models.TextField(max_length=200,null=True)



class Room(models.Model):
    type = models.CharField(max_length=250, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    code = models.IntegerField( null=True)
    def __str__(self):
        return self.name
    @property
    def image_URL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




class Reserve(models.Model):
    name=models.CharField(max_length=250,null=True)
    roomcode=models.CharField(max_length=5,null=True)
    email=models.EmailField()
    date=models.DateField(max_length=100, null=True)

class Blog(models.Model):
    name=models.CharField(max_length=100,null=True)
    content=models.TextField()
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def image_URL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


#
#
# class Profile(models.Model):
#
#     user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
#     username=models.CharField(null=True,max_length=2000)
#     firstname=models.CharField(max_length=200,null=True)
#     lastname=models.CharField(max_length=200,null=True)
#     email=models.EmailField(unique=True,null=True)
#     phone=models.CharField(max_length=10,null=True)
#     profile_pic=models.FileField(upload_to='static/infoo',default='static/images/21.jpg')
#     created_date=models.DateTimeField(auto_now_add=True)
#
#
#     def __str__(self):
#         return  self.username
#
#






