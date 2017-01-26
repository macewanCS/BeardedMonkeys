from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the demo index!!!!1")
    context = { 'diceroll': str(random.randint(1,6)) }
    return render(request, 'epl/index.html', context)
    
