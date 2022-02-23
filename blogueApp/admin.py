from ast import Subscript
from django.contrib import admin


from .models import Post, Category, Profile, Comment, Subscribers
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Subscribers)

#Unregister your models here.
admin.site.unregister(Group)