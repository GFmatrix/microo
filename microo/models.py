from django import forms
from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services')

    def __str__(self):
        return self.title

class Header(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='header')

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about')

    def __str__(self):
        return self.title
      
class Mics(models.Model):
  image = models.ImageField(upload_to='mics')
  
class Comments(models.Model):
  message = models.TextField()
  
  def __str__(self):
    return self.name

class Settings(models.Model):
  logo = models.ImageField(upload_to='settings')
  address = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  email = models.EmailField()
  
  facebook_link = models.CharField(max_length=100)
  instagram_link = models.CharField(max_length=100)
  twitter_link = models.CharField(max_length=100)

class Newsletter(models.Model):
  email = models.EmailField()

class ReqCallBack(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  phone = forms.CharField(max_length=100)
  message = forms.CharField(max_length=100)
  
  def __str__(self):
    return self.name