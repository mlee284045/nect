from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from matchmaker.forms import PersonForm
import stripe
from nect import settings


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


def profile(request):
    return render(request, 'profile.html')


def upgrade(request):
    return render(request, 'upgrade.html')

def register(request):
    print 'worked till here'
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            print form
            current_user = form.save()
            current_user.set_default()
            if request.is_ajax():
                return HttpResponse('OK')
            else:
                pass
            # current_user.email_user('Welcome!', 'Thanks for joining our website.', settings.DEFAULT_FROM_EMAIL)
    else:
        form = PersonForm()
        print 'got the empty form'
    return render(request, 'registration/register.html', {'form': form},)


def view_all(request):


    return render(request, 'view_all.html')


def view_profile(request, profile_id):
    pass
