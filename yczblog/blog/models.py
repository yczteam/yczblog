from pymodm import MongoModel, fields
from django.core.mail import send_mail
from pymodm.base.models import EmbeddedMongoModel


# Create your models here.
class User(MongoModel):
    email = fields.EmailField(required=True, primary_key = True)
    username = fields.CharField(max_length=50, required=True)
    password = fields.CharField(max_length=50, required=True)
    firstname = fields.CharField(max_length=50, required = True)
    middlename = fields.CharField(max_length=50)
    surname = fields.CharField(max_length=50, required=True)
    roles = fields.ListField()
    createtime = fields.DateTimeField()
    
    class Meta:
        connection_alias = 'ycz-blog'
        
    def get_full_name(self):

        full_name = self.firstname + " " + self.middlename + " " + self.lastname
        return full_name.strip()
    
    def get_short_name(self):

        return self.firstname

    def email_user(self, subject, message, fromemail=None, **kwargs):

        send_mail(subject, message, fromemail, [self.email], **kwargs)
    
    def __str__(self):
        return self.email
    
    def __unicode__(self):
        return self.email
    

class Comment(EmbeddedMongoModel):
    author = fields.ReferenceField(User)
    commentedon = fields.DateTimeField()
    content = fields.CharField()
    
    class Meta:
        connection_alias = 'ycz-blog'


class Post(MongoModel):
    title = fields.CharField()
    author = fields.ReferenceField(User)
    postedon = fields.DateTimeField()
    content = fields.CharField()
    tags = fields.ListField()
    comments = fields.EmbeddedDocumentListField(Comment)
    
    class Meta:
        connection_alias = 'ycz-blog'
    
    
    
