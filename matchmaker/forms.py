from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from matchmaker.models import Person


class PersonForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = Person

        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]