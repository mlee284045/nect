from django.contrib import admin

# Register your models here.
from matchmaker.models import Person, Passion, Photo, Like


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Passion)
class PassionAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass