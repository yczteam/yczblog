'''
Created on Dec 31, 2016

@author: Yunus Emrah Bulut
'''

from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    
    url(r'^postContent/(?P<post_id>[0-9a-f]+)$', views.postContent, name='postContent'),
    url(r'^writepost/', views.writePost, name='writePost'),
    url(r'^savepost/', views.savePost, name='savePost'),
    url(r'^signup/', views.signUp, name='signUp'),
    url(r'^signin/', views.signIn, name='signIn'),
    url(r'^signOut/', views.signOut, name='signOut'),
    url(r'^register/', views.register, name='register'),
    url(r'^checkUser/', views.checkUser, name='checkUser'),
    url(r'^', views.main, name='main'), 
]

