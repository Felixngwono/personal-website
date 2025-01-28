from django.contrib import admin
from django.urls import path
from .views import ContactusPage, blog, me,index,signup,loginpage,AdminsDashboard,logoutuser,Portfolio,events,gallery,about
urlpatterns = [
    path('',me,name='me' ),
    path('index/',index,name='index' ),
    path("signup/",signup, name="signup"),
    path("login/",loginpage, name="login"),
    path("logoutuser/",logoutuser, name="logoutuser"),
    path("blog/",blog, name="blog"),   
    path("portfolio/",Portfolio, name="portfolio"),
    path("contact_us/",ContactusPage, name="contactus"),
    path("events/",events, name="events"),
    path("about/", about, name="about"),
    path("gallery/", gallery, name="gallery"),
    path("admins/", AdminsDashboard, name="admins"),

]