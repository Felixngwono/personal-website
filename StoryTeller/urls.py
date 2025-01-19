from django.contrib import admin
from django.urls import path
from .views import ContactusPage, blog, me,index,signup,loginpage,logoutuser,Portfolio
urlpatterns = [
    path('',me,name='me' ),
    path('index/',index,name='index' ),
    path("signup/",signup, name="signup"),
    path("login/",loginpage, name="login"),
    path("logoutuser/",logoutuser, name="logoutuser"),
    path("blog/",blog, name="blog"),   
    path("portfolio/",Portfolio, name="portfolio"),
    path("contact_us/",ContactusPage, name="contactus"),

    

    
]