from django.contrib.auth.models import User
from django.db import models

class Passion(models.Model):
    name = models.CharField(max_length=40)
    details = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Person(User):
    gender = models.NullBooleanField(null=True)  # true will be male and false will be female
    location = models.CharField(blank=True, max_length=60)
    bio = models.TextField(blank=True, )
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    account = models.BooleanField(default=False)  # true means paid account and false means unpaid account
    # also need to make sure that the user can't change this by themselves in forms
    passions = models.ManyToManyField(Passion, related_name='users')

    def removePassion(self, name):
        passion = self.passions.objects.get(name=name)
        passion.users.remove(self)

    def __unicode__(self):
        return self.username


class Photo(models.Model):
    title = models.CharField(max_length=120)
    profile = models.BooleanField(default=False)
    img = models.URLField()
    user = models.ForeignKey(User, related_name='photos')

    def __unicode__(self):
        return self.title


class Like(models.Model):
    user_key = models.PositiveIntegerField()
    user = models.ForeignKey(User, related_name='likes')





