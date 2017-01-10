from .models import User, Post, Comment
import pymongo
from bson.objectid import ObjectId


# Create your models here.

def getLastNBlogPosts(n):
    
    posts = Post.objects.all().order_by([("postedon",pymongo.DESCENDING)]).limit(n)
    return posts

def registerUser(email, username, password, firstname, middlename, surname, createtime):
    
    User(email, username, password, firstname, middlename, surname, createtime).save()
    

def getUserByEmailAndPassword(email, password):
    
    return User.objects.raw({"_id": email, "password": password})

def getUserByEmail(email):
    
    return User.objects.raw({"_id": email})

def getPostById(postId):
    
    return Post.objects.raw({"_id":ObjectId(postId)})[0]

def savePost(title, user, postedon, blogpost, tags):
    
    Post(title = title, author = user, postedon = postedon, content = blogpost, tags = tags).save()
    
        

    
    