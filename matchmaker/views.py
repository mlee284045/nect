from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from matchmaker.forms import PersonForm
from nect import settings


def home(request):
    return render(request, 'index.html')


def login(request):
    return render_to_response(request, 'login.html', )


def logout(request):
    return render_to_response(request, 'logout.html', )


def profile(request):
    print request.user
    return render_to_response(request, 'profile.html', )


def register(request):
    print 'worked till here'
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            current_user = form.save()
            # current_user.email_user('Welcome!', 'Thanks for joining our website.', settings.DEFAULT_FROM_EMAIL)

            return redirect('profile')
    else:
        form = PersonForm()
        print 'got the empty form'
    return render(request, 'registration/register.html', {'form': form},)


def view_all(request):
    pass


def view_profile(request, profile_id):
    pass
