from .models import User, Post, Comment
import pymongo


# Create your models here.

def getLastNBlogPosts(n):
    
    posts = Post.objects.all().order_by([("postedon",pymongo.DESCENDING)]).limit(n)
    return posts

def registerUser(email, username, password, firstname, middlename, surname, createtime):
    
    User(email, username, password, firstname, middlename, surname, createtime).save()
    

def getUserByEmailAndPassword(email, password):
    
    return User.objects.raw({"_id": email, "password": password})

    
    