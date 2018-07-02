from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

class ArticlePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='POST_IMAGE/', blank=True)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class ArtistPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='POST_IMAGE/', blank=True)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class ArtistProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='POST_IMAGE/', blank=True)
    location = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    bio = models.TextField(null=True, blank=True)

def __str__(self):
        return self.user

class FanProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='POST_IMAGE', blank=True)
    location = models.CharField(max_length=150)
    age = models.CharField(max_length=2)
    bio = models.TextField(null=True, blank=True)


def __str__(self):
        return self.user.username

class ContributerProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='POST_IMAGE', blank=True)
    location = models.CharField(max_length=150)
    age = models.CharField(max_length=2)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username









#class ArtistClass(models.Model):
    #user =








#class ContributerPage(models.Model):






#class WhatsNew(models.Model):

# Create your models here.
