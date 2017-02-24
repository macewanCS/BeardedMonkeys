from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse
from .forms import HardwareTicketForm, SoftwareTicketForm
# import models
from epl.models import CallLog


def index(request):
    #return HttpResponse("Hello, world. You're at the demo index!!!!1")
    context = { 'diceroll': str(random.randint(1,6)) }
    return render(request, 'epl/index.html', context)

def hardware(request):
    #number = random.randint(1,6)
    #numberData = CallLog(Severity = number)
    #numberData.save()
    
    context = {}
    #return render(request, 'epl/hardware.html', context)
    form_class = HardwareTicketForm
    return render(request, 'epl/hardware.html', {
        'form': form_class,
    })

def software(request):
    context = {}
    #return render(request, 'epl/software.html', context)
    form_class = SoftwareTicketForm
    return render(request, 'epl/software.html', {
        'form': form_class,
    })
    

def service(request):
    context = {}
    return render(request, 'epl/service.html', context)

def general(request):
    context = {}
    return render(request, 'epl/general.html', context)

def password(request):
    context = {}
    return render(request, 'epl/password.html', context)

def login(request):
    context = {}
    return render(request, 'epl/login.html', context)

def manage(request):
    # retriving all the data
    tickets = CallLog.objects.all()
    
    context = { "tickets" : tickets }
    return render(request, 'epl/manage-tickets.html', context)

