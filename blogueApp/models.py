from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.


#Newsletter
class Subscribers(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-list', kwargs={'cats': self.name})

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) #One to one association with user model in members directory
    bio = models.TextField()
    headline = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user) 

    
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    # category = models.CharField(max_length=255, default="Others")
    category = models.ForeignKey(Category ,max_length=60 ,default='Others', on_delete=models.CASCADE, related_name= 'cats')
    likes = models.ManyToManyField(User, related_name='blog_post')
    article_image = models.ImageField(null=True, blank=True, upload_to="images/")


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.username)
        