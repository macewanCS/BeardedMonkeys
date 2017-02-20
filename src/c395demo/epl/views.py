from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the demo index!!!!1")
    context = { 'diceroll': str(random.randint(1,6)) }
    return render(request, 'epl/index.html', context)
    
def hardware(request):
    context = {}
    return render(request, 'epl/hardware.html', context)
    
def software(request):
    context = {}
    return render(request, 'epl/software.html', context)

def login(request):
    context = {}
    return render(request, 'epl/login.html', context)

def manage(request):
    context = {}
    return render(request, 'epl/manage.html', context)

