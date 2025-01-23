from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(models.Model): 
    mygender= (
        ('male','male'),
        ('female','female'),
        ('others','others')
    )
    name= models.CharField(max_length=100)
    bio=models.TextField()
    profilepic=models.ImageField(upload_to='profile',default="avatar.png")
    birthdate=models.DateField(auto_now=False, null=True, blank=True)
    gender=models.CharField(max_length=10,choices=mygender)
    email= models.EmailField()
    is_superuser=models.BooleanField(default=False)
    is_enduser= models.BooleanField(default=False)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = []

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()
        
    def __str__(self):
            return self.name
        
        
class BlogPost(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class PortfolioItem(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='portfolio_images/')
    url=models.URLField()
    
    def __str__(self):
        return self.title


class events(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='events_images/')
    date=models.DateTimeField()
    
    def __str__(self):
        return self.title
    