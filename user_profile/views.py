from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from forms import RegistrationForm, ProfileSettingsForm

@login_required(login_url='/accounts/login/')
def signin(request):
    if request.user.is_authenticated():
        return HttpResponse('alles ok')
    else:
        return HttpResponseRedirect('/accounts/login/')
    return HttpResponse('hmm')
    
from django.core.mail import send_mail
def sendmail(request):
    send_mail('hallo', 'whats up', 'kuzma@allink.ch', ['kuzma@allink.ch'], fail_silently=False)
    return HttpResponseRedirect('/')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})
    
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')
        
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/logout/')
   
@login_required(login_url='/accounts/login/') 
def profile_settings(request):
    form = ProfileSettingsForm()
    return render(request, 'profile_settings.html', {'form': form})