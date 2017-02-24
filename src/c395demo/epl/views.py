from django.shortcuts import render
import random

from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from .forms import HardwareTicketForm, SoftwareTicketForm
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
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')    
    
    #return HttpResponse("Hello, world. You're at the demo index!!!!1")
    context = { 'diceroll': str(random.randint(1,6)) }
    return render(request, 'epl/index.html', context)

# harware tickets page view
def hardware(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')
        
    #example of how to save data
    #number = random.randint(1,6)
    #numberData = CallLog(Severity = number)
    #numberData.save()
    
    context = {}
    #return render(request, 'epl/hardware.html', context)
    form_class = HardwareTicketForm
    return render(request, 'epl/hardware.html', {
        'form': form_class,
    })

# software tickets page view
def software(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')
    
    context = {}
    #return render(request, 'epl/software.html', context)
    form_class = SoftwareTicketForm
    return render(request, 'epl/software.html', {
        'form': form_class,
    })
    

# service tickets page view
def service(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')
    
    context = {}
    return render(request, 'epl/service.html', context)

# general tickets page view
def general(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')
        
    context = {}
    return render(request, 'epl/general.html', context)

# password recovery tickets page view
def password(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')
        
    context = {}
    return render(request, 'epl/password.html', context)

# manage all tickets page view
def manage(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')
        
    # retriving all the data
    tickets = CallLog.objects.all()
    
    context = { "tickets" : tickets }
    return render(request, 'epl/manage-tickets.html', context)

# login and user authentication

# login page view
def login_view(request):
    form = UserLogin(request.POST or None)
    
    if (request.user.is_authenticated()):
        return redirect('/')
    
    # check if the input is valid
    if (form.is_valid()):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username=username, password=password)
        
        login(request, user)
        
        return redirect('/')
        
    context = { "form" : form, "name" : "Login" }
    return render(request, 'epl/login.html', context)

# logout page view
def logout_view(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')
    
    logout(request)
    context = {}
    return render(request, 'epl/logout.html', context)

