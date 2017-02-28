from datetime import datetime
from django.shortcuts import render
import random

from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from .forms import HardwareTicketForm, SoftwareTicketForm
# import models
from epl.models import CallLog, Asgnmnt, ProbType

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
        
    form = HardwareTicketForm(request.POST or None)
    if form.is_valid():
        # saving data into the database
        msg = database_saved(form, request.user.username)
    
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
    callLogs = CallLog.objects.all()
    asgnmnts = Asgnmnt.objects.all()
    probTypes = ProbType.objects.all()
    
    context = { 
        "callLogs" : callLogs,
        "asgnmnts" : asgnmnts,
        "probTypes" : probTypes
        }
    return render(request, 'epl/manage-tickets.html', context)
    
def detail(request, id):
    ticket = CallLog.objects.get(CallID = id)
    
    recvdDate = "20"
    recvdDate += ticket.RecvdDate
    
    temp = parsing(ticket.Symptoms, "`")
    
    context = {
        "CallID" : ticket.CallID,
        "CustID" : ticket.CustID,
        "Symptoms" : ticket.Symptoms,
        "RecvdDate" : recvdDate,
        "EquipType" : temp[0],
        "AssetTag" : temp[1],
        "DeviceName" : temp[2],
        "Description" : temp[3],
        "ErrorMsg" : temp[4],
        "Category" : ticket.Category,
        "CallStatus" : ticket.CallStatus,
        "Priority" : ticket.Priority
    }
    return render(request, 'epl/view-ticket.html', context)

#---------------------------------
# login and user authentication
#---------------------------------

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

def parsing(string, parse):
    return string.split(parse)
    
#------------------------------------
# data saving for hardware tickets
#------------------------------------

# saving data into database
def database_saved(form, username):
    try:
        # getting data from the form
        asset_tag = form.cleaned_data.get("asset_tag")
        equipment_type = form.cleaned_data.get("equipment_type")
        problem_description = form.cleaned_data.get("problem_description")
        error_messages = form.cleaned_data.get("error_messages")
        file_upload = form.cleaned_data.get("file_upload")
        device_name = form.cleaned_data.get("device_name")

        # equipment type
        probType_ProbType = equipment_type
        callLog_Symptoms = equipment_type
        asgnmnt_Description = equipment_type

        # asset tag
        callLog_Symptoms += "`"
        asgnmnt_Description += "`"
        callLog_Symptoms += asset_tag
        asgnmnt_Description += asset_tag

        # device name
        callLog_Symptoms += "`"
        asgnmnt_Description += "`"
        callLog_Symptoms += device_name
        asgnmnt_Description += device_name

        # description of the problem
        callLog_Symptoms += "`"
        asgnmnt_Description += "`"
        callLog_Symptoms += problem_description
        asgnmnt_Description += problem_description

        # error messages
        callLog_Symptoms += "`"
        asgnmnt_Description += "`"
        callLog_Symptoms += error_messages
        asgnmnt_Description += error_messages

        # priority
        if ( equipment_type == "Sorter" ):
            callLog_Priority = "1"
            
        elif( equipment_type == "Smart Chute" or 
            equipment_type == "Self-checkout" ):
            callLog_Priority = "2"
            
        else:
            callLog_Priority = "3"

        # call source
        callLog_CallSource = "Web"

        # assigned team name
        if( equipment_type == "PC" or 
            equipment_type == "Laptop" ):
            asgnmnt_TeamName = "Help Desk Team"
            
        else:
            asgnmnt_TeamName = "Project Team"

        # assigned by
        asgnmnt_AssignedBy = "Selfserve"

        # assignment status
        asgnmnt_Status = "Unacknowledged"

        # current timestamp
        temp = parsing(str(datetime.now()), " ")
        callLog_RecvdDate = temp[0][2:]
        callLog_RecvdTime = callLog_RecvdDate
        asgnmnt_DateAssign = callLog_RecvdDate
        asgnmnt_TimeAssign = callLog_RecvdDate

        # user ID
        callLog_CustID = username

        # tracker
        callLog_Tracker = "selfserve"

        # call log status
        callLog_Status = "Open"

        # CallLog Table
        callLog_table = CallLog(
            Symptoms = callLog_Symptoms,
            Priority = callLog_Priority,
            CallSource = callLog_CallSource,
            RecvdDate = callLog_RecvdDate,
            RecvdTime = callLog_RecvdTime,
            CustID = callLog_CustID,
            Tracker = callLog_Tracker,
            CallStatus = callLog_Status,
            Category = "Hardware"
        )

        # Asgnmnt Table
        asgnmnt_table = Asgnmnt(
            Description = asgnmnt_Description,
            TeamName = asgnmnt_TeamName,
            AssignedBy = asgnmnt_AssignedBy,
            Status = asgnmnt_Status,
            DateAssign = asgnmnt_DateAssign,
            TimeAssign = asgnmnt_TimeAssign
        )

        # ProbType Table
        probType_table = ProbType(
            ProbType = probType_ProbType
        )

        # Saving data into the database
        callLog_table.save()
        asgnmnt_table.save()
        probType_table.save()
            
        return "Ticket added sucessfully"
        
    except:
        return "Something went wrong"

