from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
# class SuperUser(models.Model):
#     pass

class BlogPost(models.Model):

    Author = models.ForeignKey('auth.User')
    Title = models.CharField(max_length=200,blank=False)
    PostContent = models.TextField(blank=False)
    CreationDate = models.DateTimeField(default=timezone.now())
    PublishDate = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.PublishDate = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(ApprovedComment=True)

    def __str__(self):
        return self.Title

class Comments(models.Model):

    Post = models.ForeignKey('BlogApp.BlogPost',related_name='comment')
    UserName = models.CharField(max_length=50)
    Text = models.TextField()
    CreationDate = models.DateTimeField(default=timezone.now())
    ApprovedComment = models.BooleanField(default=False)
    
    def approve(self):
        self.ApprovedComment = True
        self.save()

    def __str__(self):
        return self.Text
