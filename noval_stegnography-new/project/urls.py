"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('home',views.home,name='home'),
    # path('approveuser/home',views.home,name='home2'),
    path('signup',views.signup,name='signup'),
    path('signupaction',views.signupaction,name='signupaction'),
    path('login',views.login,name='login'),
    path('loginaction',views.loginaction,name='loginaction'),
    path('logout',views.custom_logout,name='custom_logout'),
    path('approveuser/logout',views.custom_logout,name='custom_logout1'),
    path('editlogin/<int:id>',views.editlogin,name='editlogin'),
    path('updatelogin/<int:id>',views.updatelogin,name='updatelogin'),
    path('deletelogin/<int:id>',views.deletelogin,name='deletelogin'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('updatepassword',views.updatepassword,name='updatepassword'),
    path('validateuser',views.validateuser,name='validateuser'),
    path('approveuser/<str:username>',views.approveuser,name='approveuser'),
    path('rejectuser/<str:username>',views.rejectuser,name='rejectuser'),
    path('editusers',views.editusers,name='editusers'),
    path('',views.home1,name='home1'),
     path('aaa',views.aaa,name='aaa'),
    #   path('aaa',views.aaa,name='aaa'),
     path('hide/',views.HideMessageView.as_view(), name='hide'),
    path('decrypt/', views.decrypt, name='decrypt'),
    

    


    
]
