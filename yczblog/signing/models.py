from django.db import models
from mongoengine.document import Document
from mongoengine.fields import StringField, EmailField, ListField, DateTimeField
from django.db.models.fields.files import ImageField
from datetime import datetime


# Create your models here.
class User(Document):
    email = EmailField(required=True, primary_key = True)
    user_name = StringField(max_length=50, required=True)
    first_name = StringField(max_length=50, required = True)
    middle_name = StringField(max_length=50)
    surname = StringField(max_length=50, required=True)
    avatar = ImageField(width_field=600, height_field=600)
    roles = ListField()
    create_time = datetime.utcnow()
    
    def __str__(self):
        return self.email