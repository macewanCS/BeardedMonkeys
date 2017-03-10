import json
from datetime import datetime
from django.shortcuts import render
import random

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
from .forms import *
# import models
from epl.models import *

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

    username = get_username(request)

    context = { 'username': username }
    return render(request, 'epl/index.html', context)

# add ticket page
def add(request):
    context = {}
    return render(request, 'epl/add-ticket.html', context)

# harware tickets page view
def hardware(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')

    form = HardwareTicketForm(request.POST or None)
    if form.is_valid():
        # saving data into the database
        msg = database_saved(form, request.user.username)

        # Get the hardware ticket Id and redirect to the successful
        # submission page with the hardware ticket info
        ticketId = getTicketId("Hardware", request.user.username)
        context = successTicketSummary(request, ticketId)
        return render(request, "epl/hardware_submitted.html", context)

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

    form = SoftwareTicketForm(request.POST or None)
    if form.is_valid():
        # saving data into the database
        msg = soft_database_saved(form, request.user.username)

        # Get the software ticket Id and redirect to the successful
        # submission page with the software ticket info
        ticketId = getTicketId("Software", request.user.username)
        context = successTicketSummary(request, ticketId)
        return render(request, "epl/software_submitted.html", context)

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
    
    form = PasswordTicketForm(request.POST or None)
    if form.is_valid():
        # saving data into the database
        msg = pass_database_saved(form, request.user.username)

        # Get the hardware ticket Id and redirect to the successful
        # submission page with the hardware ticket info
        ticketId = getTicketId("Password", request.user.username)
        context = successTicketSummary(request, ticketId)
        return render(request, "epl/hardware_submitted.html", context)
    
    context = {'form': PasswordTicketForm}
    return render(request, 'epl/password.html', context)

# my all tickets page view
def tickets(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')

    # retriving all the data
    username = request.user.username
    callLogs = CallLog.objects.filter(CustID=username)

    context = {
        "callLogs" : callLogs,
        "available" : ["Hardware", "Software", "Service", "Other", "Password"]
        }
    return render(request, 'epl/my-tickets.html', context)

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
        "probTypes" : probTypes,
        "available" : ["Hardware", "Software", "Service", "Other", "Password"]
        }
    return render(request, 'epl/manage-tickets.html', context)

def detail(request, id):
    ticket = CallLog.objects.get(CallID = id)

    recvdDate = "20"
    recvdDate += ticket.RecvdDate

    temp = parsing(ticket.Symptoms, "|")

    if ( len(temp) <= 1 ):
        temp = parsing(ticket.Symptoms, "`")

    if ( ticket.Category == "Hardware" ):
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

    elif ( ticket.Category == "Software" ):
        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "RecvdDate" : recvdDate,
            "System" : temp[0],
            "Offline" : temp[1],
            "Description" : temp[2],
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority
        }
        
    elif ( ticket.Category == "Password" ):
        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "RecvdDate" : recvdDate,
            "System_type" : temp[0],
            "Sys_user" : temp[1],
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority
        }

    else:
        context = {}

    return render(request, 'epl/view-ticket.html', context)

# return the active username
def get_username(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

    return username

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

# function parse a string
def parsing(string, parse):
    return string.split(parse)

# resolved ticket status

def resolved(ticket_id):
    ticket = CallLog.objects.get(CallID=ticket_id)
    
    if ( ticket.CallStatus == "Open" ):
        ticket.CallStatus = "Resolved"
    else:
        ticket.CallStatus = "Open"

    ticket.save()
    context = {}
    return render(request, 'epl/manage-tickets.html', context)

#-----------------------------------
# Functions to get the ticket Ids
#-----------------------------------
def getTicketId(ticketCategory, username):
    callLogs = CallLog.objects.all()
    callLogId = 0
    for callLog in callLogs:
        if (callLog.CustID == username):
            if (callLog.Category == ticketCategory):
                callLogId = callLog.CallID
    return callLogId

def successTicketSummary(request, id):
    ticket = CallLog.objects.get(CallID = id)

    recvdDate = "20"
    recvdDate += ticket.RecvdDate

    temp = parsing(ticket.Symptoms, "|")

    if ( len(temp) <= 1 ):
        temp = parsing(ticket.Symptoms, "`")

    if ( ticket.Category == "Hardware" ):
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
        
    elif ( ticket.Category == "Password" ):
        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "RecvdDate" : recvdDate,
            "system_type" : temp[0],
            "sys_user" : temp[1],
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority
        }

    elif ( ticket.Category == "Software" ):
        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "RecvdDate" : recvdDate,
            "System" : temp[0],
            "Offline" : temp[1],
            "Description" : temp[2],
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority
        }

    else:
        context = {}

    return context

#------------------------------------
# data saving for hardware tickets
#------------------------------------

# saving password data into database
def pass_database_saved(form, username):
    try:
        # getting data from the form
        system_type = form.cleaned_data.get("system_type")
        sys_user = form.cleaned_data.get("sys_user")

        # system type
        probType_ProbType = system_type
        callLog_Symptoms = system_type
        asgnmnt_Description = system_type

        # system user
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += sys_user
        asgnmnt_Description += sys_user

        # priority
        if ( system_type == "StaffWeb/Active Directory"
            or system_type == "Dayforce" ):
            callLog_Priority = "2"

        else:
            callLog_Priority = "3"

        # call source
        callLog_CallSource = "Web"

        # assigned team name
        asgnmnt_TeamName = "Help Desk Team"

        # assigned by
        asgnmnt_AssignedBy = "Selfserve"

        # assignment status
        asgnmnt_Status = "Unacknowledged"

        # current timestamp
        temp = parsing(str(datetime.now()), " ")
        callLog_RecvdDate = temp[0][2:]
        callLog_RecvdTime = temp[1][:8]
        asgnmnt_DateAssign = temp[0][2:]
        asgnmnt_TimeAssign = temp[1][:8]
        
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
            Category = "Password"
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

# saving hardware data into database
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
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += asset_tag
        asgnmnt_Description += asset_tag

        # device name
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += device_name
        asgnmnt_Description += device_name

        # description of the problem
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += problem_description
        asgnmnt_Description += problem_description

        # error messages
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"

        if ( error_messages == "" or error_messages == " " ):
            error_messages = "NULL"

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
        callLog_RecvdTime = temp[1][:8]
        asgnmnt_DateAssign = temp[0][2:]
        asgnmnt_TimeAssign = temp[1][:8]

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

# saving data into database for software
def soft_database_saved(form, username):
    try:
        # getting data from the form
        system = form.cleaned_data.get("system")
        system_offline = form.cleaned_data.get("system_offline")
        problem_description = form.cleaned_data.get("problem_description")
        steps_replicate_problem = form.cleaned_data.get("steps_replicate_problem")
        file_upload = form.cleaned_data.get("file_upload")

        # system type
        probType_ProbType = system
        callLog_Symptoms = system
        asgnmnt_Description = system


        # offline/broken
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += system_offline
        asgnmnt_Description += system_offline


        # description of problem
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += problem_description
        asgnmnt_Description += problem_description

        # priority
        if ( system_offline == "Yes" ):
            callLog_Priority = "1"
        else:
            callLog_Priority = "3"

        # call source
        callLog_CallSource = "Web"


        # assigned team name
        if( probType_ProbType == "Internet/Network" or probType_ProbType=="S:/ drive"):
            asgnmnt_TeamName = "Netwrok Team"


        elif( probType_ProbType == "Workflows"):
            asgnmnt_TeamName = "ILS Team"

        else:
            asgnmnt_TeamName = "Help Desk Team"


        # assigned by
        asgnmnt_AssignedBy = "Selfserve"


        # assignment status
        asgnmnt_Status = "Unacknowledged"

        # current timestamp
        temp = parsing(str(datetime.now()), " ")
        callLog_RecvdDate = temp[0][2:]
        callLog_RecvdTime = temp[1][:8]
        asgnmnt_DateAssign = temp[0][2:]
        asgnmnt_TimeAssign = temp[1][:8]

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
            Category = "Software"
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

@csrf_exempt
def alter_status(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        id = request.POST.get('id')

        print (id, status)

        response_data = {}

        calllog = CallLog.objects.get(CallID=id)
        calllog.CallStatus = status
        calllog.save()

        response_data['result'] = 'Create post successful!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

