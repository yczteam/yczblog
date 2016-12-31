'''
Created on Dec 31, 2016

@author: Yunus Emrah Bulut
'''

from django.conf.urls import url

from . import views

app_name = 'signing'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signUp, name='signUp'),
    url(r'^signin/', views.signIn, name='signIn'),

]

