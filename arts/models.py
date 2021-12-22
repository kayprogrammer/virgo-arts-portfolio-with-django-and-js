from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.

class Art(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    pic = CloudinaryField('image', null=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)

class Virgo(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    address = models.TextField(max_length=1000, null=True)
    facebook = models.URLField(max_length=500, null=True)
    twitter = models.URLField(max_length=500, null=True)
    instagram = models.URLField(max_length=500, null=True)
    whatsapp = models.URLField(max_length=500, null=True)
    linkedin = models.URLField(max_length=500, null=True)
    map_link = models.URLField(max_length=1000, null=True) 
    avatar = CloudinaryField('image', null=True)

    def __str__(self):
        return str(self.name)

    def avatarURL(self):
        try:
            url = self.avatar.url
        except:
            url = ""
        return url

class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    message = models.TextField(max_length=5000, null=True)
    date_sent = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.name)

class About(models.Model):
    title1 = models.CharField(max_length=100, null=True)
    title2 = models.CharField(max_length=100, null=True)
    about1 = RichTextField(config_name= 'awesome_ckeditor', null=True)
    about2 = RichTextField(config_name= 'awesome_ckeditor', null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    image1 = CloudinaryField('image', null=True)
    image2 = CloudinaryField('image', null=True)
    copywright = models.TextField(null=True)
    
    def __str__(self):
        return str(self.title1)