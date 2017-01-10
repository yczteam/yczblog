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
    
    userObj = {}
    userObj['username'] = username
    userObj['email'] = email
    request.session['user'] = userObj
    
    return main(request)

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
        #adds user to the session
        userObj = {}
        userObj['username'] = auth_user[0].username
        userObj['email'] = auth_user[0].email
        request.session['user'] = userObj
        return main(request)

def signOut(request):
    
    del request.session['user']
    #request.session.modified = True
    return main(request)

    
def postContent(request, post_id):
    
    post = services.getPostById(post_id)
    
    context = {
        'post': post,
    }
    
    return render(request, 'blog/postContent.html', context)

def writePost(request):
    
    return render(request, 'blog/writePost.html')

def savePost(request):
    
    blogpost = request.POST['blogpost']
    email = request.session['user']['email']
    user = services.getUserByEmail(email)[0]
    title = "standart başlık"
    postedon = datetime.datetime.now()
    tags = ['yazılım','yapay zeka']
    
    services.savePost(title, user, postedon, blogpost, tags)
    
    return main(request)
    
    


