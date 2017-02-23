from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse
# import models
from epl.models import CallLog

# import for user authentication
from .forms import UserLogin
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )

# main index view
def index(request):
    #return HttpResponse("Hello, world. You're at the demo index!!!!1")
    context = { 'diceroll': str(random.randint(1,6)) }
    return render(request, 'epl/index.html', context)

# harware tickets page view
def hardware(request):
    #example of how to save data
    #number = random.randint(1,6)
    #numberData = CallLog(Severity = number)
    #numberData.save()
    
    context = {}
    return render(request, 'epl/hardware.html', context)

# software tickets page view
def software(request):
    context = {}
    return render(request, 'epl/software.html', context)

# service tickets page view
def service(request):
    context = {}
    return render(request, 'epl/service.html', context)

# general tickets page view
def general(request):
    context = {}
    return render(request, 'epl/general.html', context)

# password recovery tickets page view
def password(request):
    context = {}
    return render(request, 'epl/password.html', context)

# manage all tickets page view
def manage(request):
    # retriving all the data
    tickets = CallLog.objects.all()
    
    context = { "tickets" : tickets }
    return render(request, 'epl/manage-tickets.html', context)

# login and user authentication

# login page view
def login_view(request):
    login = UserLogin(request.POST or None)
    
    # check if the input is valid
    if (login.is_valid()):
        username = login.cleaned_data.get("username")
        password = login.cleaned_data.get("password")
        
    context = { "form" : login, "name" : "Login" }
    return render(request, 'epl/login.html', context)

# logout page view
def logout_view(request):
    context = {}
    return render(request, 'epl/login.html', context)

