# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from asyncio.base_subprocess import WriteSubprocessPipeProto
from django.db import models
from django.contrib.auth.models import User

#supporting func
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'
#create model class User
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.username


class UserSocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='SocialMediaUser')
    network = models.CharField(max_length=200)
    title = models.CharField(max_length=250)
    href = models.URLField()
    
class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='LocationUser')
    address = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=250)
    type = models.CharField(max_length=250)

class Job(models.Model):
    organization = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    url = models.URLField()
    startDate = models.DateField()
    endDate = models.DateField()
    summary = models.CharField(max_length=2200)
    highlights = models.CharField(max_length=2200)

class VolunteerWork(models.Model):
    organization = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    url = models.URLField()
    startDate = models.DateField()
    endDate = models.DateField()
    summary = models.CharField(max_length=2200)
    highlights = models.CharField(max_length=2200)

class LiveResume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='LiveResumeUser')    
    fullname = models.CharField(max_length=250)
    label = models.CharField(max_lenght=250)
    phone = models.CharField(max_length=10)
    dob = models.DateField()
    url = models.URLField()
    locations = models.ForeignKey(UserLocation, on_delete=models.CASCADE, related_name='UserLocations')
    socialMedia = models.ForeignKey(UserSocialMedia, on_delete=models.CASCADE, related_name='UserSocialMedias')
    summary = models.CharField(max_length=2000)
    image = models.ImageField
    work = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='UserJobs')
    volunteer = models.ForeignKey(VolunteerWork, on_delete=models.CASCADE, related_name='UserVolunteers')
