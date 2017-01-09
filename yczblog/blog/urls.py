'''
Created on Dec 31, 2016

@author: Yunus Emrah Bulut
'''

from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    
    url(r'^signup/', views.signUp, name='signUp'),
    url(r'^signin/', views.signIn, name='signIn'),
    url(r'^register/', views.register, name='register'),
    url(r'^checkUser/', views.checkUser, name='checkUser'),
    url(r'^', views.main, name='main'), 
]

