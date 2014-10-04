from django.contrib.auth.models import User
from django.db import models

class Passion(models.Model):
    pass
    name = models.CharField(max_length=40)
    details = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Person(User):
    pass
    gender = models.BooleanField(default=True)  # true will be male and false will be female
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    account = models.BooleanField(default=False)  # true means paid account and false means unpaid account
    passions = models.ManyToManyField(Passion, related_name='users')

    def removePassion(self, name):
        passion = self.passions.objects.get(name=name)
        passion.users.remove(self)

    def __unicode__(self):
        return self.username


class Photo(models.Model):
    pass
    title = models.CharField(max_length=120)
    profile = models.BooleanField(default=False)
    img = models.URLField()
    user = models.ForeignKey(User, related_name='photos')

    def __unicode__(self):
        return self.title


class Like(models.Model):
    pass
    user_key = models.PositiveIntegerField()
    user = models.ForeignKey(User, related_name='likes')





