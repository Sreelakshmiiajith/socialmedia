from django.db import models
from django.contrib.auth.models import User


class Uprofile(models.Model):
    uname=models.OneToOneField(User,max_length=200)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=200)
    propic=models.ImageField()
    dob=models.PositiveIntegerField()
    bio=models.CharField(max_length=100)

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="post_img",null=True)
    caption=models.CharField(max_length=200,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=300,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    


