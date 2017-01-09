# Create your views here.
from django.shortcuts import render
from .models import User, Post, Comment
import datetime
from blog import services


def main(request):
       
    posts = services.getLastNBlogPosts(3)
    
    context = {
        'latest_post_list': posts,
    }
    return render(request, 'blog/index.html', context)

def signUp(request):
    return render(request, 'blog/signup.html')

def signIn(request):
    return render(request, 'blog/signin.html')

def register(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    firstname = request.POST['firstname']
    middlename = request.POST['middlename']
    surname = request.POST['lastname']
    createtime = datetime.datetime.now()
    
    services.registerUser(email, username, password, firstname, middlename, surname, createtime)
    
    return render(request, 'blog/index.html')

def checkUser(request):
        
    email = request.POST['email']
    password = request.POST['password']
    auth_user = services.getUserByEmailAndPassword(email, password)
    
    if auth_user == None or auth_user.count()==0:
        context = {
        'error': "incorrect mail or password",
        }
        return render(request, 'blog/signin.html',context)
    else:
        
        return render(request, 'blog/signin.html')


