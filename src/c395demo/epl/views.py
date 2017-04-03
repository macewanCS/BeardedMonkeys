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
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')
    context = {}
    return render(request, 'epl/add-ticket.html', context)

# harware tickets page view
def hardware(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')

    ticketId = request.GET.get('ticketID')
    if ticketId == None:
        form = HardwareTicketForm(request.POST or None)
    else:
        context = successTicketSummary(request, ticketId, "update")
        form = HardwareTicketForm(request.POST or None, initial=context, auto_id=False)

    if form.is_valid():
        # saving data into the database
        msg = database_saved(form, request.user.username, ticketId)

        # Get the hardware ticket Id and redirect to the successful
        # submission page with the hardware ticket info
        if (ticketId == None):
            ticketId = getTicketId("Hardware", request.user.username)
            context = successTicketSummary(request, ticketId, "insert")
        else:
            context = successTicketSummary(request, ticketId, "update")

        return render(request, "epl/hardware_submitted.html", context)

    '''context = {}
    #return render(request, 'epl/hardware.html', context)
    form_class = HardwareTicketForm
    return render(request, 'epl/hardware.html', {
        'form': form_class,
    })'''
    context = {'form': form}
    return render(request, 'epl/hardware.html', context)

# software tickets page view
def software(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')

    ticketId = request.GET.get('ticketID')
    if ticketId == None:
        form = SoftwareTicketForm(request.POST or None)
    else:
        context = successTicketSummary(request, ticketId, "update")
        form = SoftwareTicketForm(request.POST or None, initial=context, auto_id=False)

    if form.is_valid():
        # saving data into the database
        msg = soft_database_saved(form, request.user.username, ticketId)

        # Get the software ticket Id and redirect to the successful
        # submission page with the software ticket info
        if (ticketId == None):
            ticketId = getTicketId("Software", request.user.username)
            context = successTicketSummary(request, ticketId, "insert")
        else:
            context = successTicketSummary(request, ticketId, "update")

        return render(request, "epl/software_submitted.html", context)

    #context = {}
    #return render(request, 'epl/software.html', context)
    #form_class = SoftwareTicketForm
    #return render(request, 'epl/software.html', {
    #    'form': form_class,
    #})
    context = {'form': form}
    return render(request, 'epl/software.html', context)


# service tickets page view
def service(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')

    ticketId = request.GET.get('ticketID')
    if ticketId == None:
        form = ServiceTicketForm(request.POST or None)
    else:
        context = successTicketSummary(request, ticketId, "update")
        form = ServiceTicketForm(request.POST or None, initial=context, auto_id=False)

    if form.is_valid():
        #saving data into the database
        msg = service_database_saved(form, request.user.username, ticketId)

        # Get the service ticket Id and redirect to the successful
        # submission page with the service ticket info
        if (ticketId == None):
            ticketId = getTicketId("Service", request.user.username)
            context = successTicketSummary(request, ticketId, "insert")
        else:
            context = successTicketSummary(request, ticketId, "update")

        return render(request, "epl/service_submitted.html", context)

    context = {'form': form}
    return render(request, 'epl/service.html', context)

# general tickets page view
def general(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')

    ticketId = request.GET.get('ticketID')
    if ticketId == None:
        form = GeneralTicketForm(request.POST or None)
    else:
        context = successTicketSummary(request, ticketId, "update")
        form = GeneralTicketForm(request.POST or None, initial=context, auto_id=False)

    if form.is_valid():
        #saving data into the database
        msg = general_database_saved(form, request.user.username, ticketId)

        # Get the general ticket Id and redirect to the successful
        # submission page with the general ticket info
        if (ticketId == None):
            ticketId = getTicketId("Other", request.user.username)
            context = successTicketSummary(request, ticketId, "insert")
        else:
            context = successTicketSummary(request, ticketId, "update")

        return render(request, "epl/general_submitted.html", context)

    context = {'form': form}
    return render(request, 'epl/general.html', context)

# password recovery tickets page view
def password(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')

    ticketId = request.GET.get('ticketID')
    if ticketId == None:
        form = PasswordTicketForm(request.POST or None)
    else:
        context = successTicketSummary(request, ticketId, "update")
        form = PasswordTicketForm(request.POST or None, initial=context, auto_id=False)

    if form.is_valid():
        # saving data into the database
        msg = pass_database_saved(form, request.user.username, ticketId)

        # Get the password ticket Id and redirect to the successful
        # submission page with the password ticket info
        if (ticketId == None):
            ticketId = getTicketId("Password", request.user.username)
            context = successTicketSummary(request, ticketId, "insert")
        else:
            context = successTicketSummary(request, ticketId, "update")

        return render(request, "epl/password_submitted.html", context)

    context = {'form': form}
    return render(request, 'epl/password.html', context)

# my all tickets page view
def tickets(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')

    # retriving all the data
    username = request.user.username
    callLogs = CallLog.objects.filter(CustID=username)

    #obtaining user's branch
    try:
        branch = UserProfile.objects.get(user=request.user).branch
    except:
        branch = "staff"
    
    available = ["Hardware", "Software", "Service", "Other", "Password"]
    count = total_count(callLogs, available)
    
    callLogs = reversed(callLogs)
    context = {
        "username" : username,
        "callLogs" : callLogs,
        "available" : available,
        "branch" : branch,
        "count" : count
    }
    return render(request, 'epl/my-tickets.html', context)

# manage all tickets page view
def manage(request):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')
    
    ticket_type = request.GET.get('ticketType')
    try:
        ticket_type = ticket_type.lower()
    except:
        ticket_type = None
    
    visible = "all"
    # retriving all the data
    if ( ticket_type == None ):
        callLogs = CallLog.objects.all()
        
    # filter based on the category of the ticket
    elif  ( ticket_type == "hardware" ):
        callLogs = CallLog.objects.filter(Category="Hardware")
        visible = "hardware"
    elif  ( ticket_type == "software" ):
        callLogs = CallLog.objects.filter(Category="Software")
        visible = "software"
    elif  ( ticket_type == "service" ):
        callLogs = CallLog.objects.filter(Category="Service")
        visible = "service"
    elif  ( ticket_type == "password" ):
        callLogs = CallLog.objects.filter(Category="Password")
        visible = "password"
    elif  ( ticket_type == "other" ):
        callLogs = CallLog.objects.filter(Category="Other")
        visible = "other"
        
    # filter based on status of the ticket
    elif  ( ticket_type == "open" ):
        callLogs = CallLog.objects.filter(CallStatus="Open")
        visible = "open"
    elif  ( ticket_type == "resolved" ):
        callLogs = CallLog.objects.filter(CallStatus="Resolved")
        visible = "resolved"
    elif  ( ticket_type == "closed" ):
        callLogs = CallLog.objects.filter(CallStatus="Closed")
        visible = "closed"
    elif  ( ticket_type == "disapproved" ):
        callLogs = CallLog.objects.filter(CallStatus="Disapproved")
        visible = "disapproved"
    elif  ( ticket_type == "needsapproval" ):
        callLogs = CallLog.objects.filter(CallStatus="Needs Approval")
        visible = "needsapproval"
    elif  ( ticket_type == "progress" ):
        callLogs = CallLog.objects.filter(CallStatus="InProgress")
        visible = "progress"
    
    else:
        callLogs = CallLog.objects.all()
    
    asgnmnts = Asgnmnt.objects.all()
    probTypes = ProbType.objects.all()
    
    # obtaining user's branch
    try:
        branch = UserProfile.objects.get(user=request.user).branch
    except:
        branch = "staff"
    
    available = ["Hardware", "Software", "Service", "Other", "Password"]
    count = total_count(callLogs, available)

    callLogs = reversed(callLogs)
    context = {
        "callLogs" : callLogs,
        "asgnmnts" : asgnmnts,
        "probTypes" : probTypes,
        "available" : available,
        "count" : count,
        "branch" : branch,
        "visible" : visible
    }
    return render(request, 'epl/manage-tickets.html', context)
    
# counts the total number of tickets
def total_count(lis, available):
    count = 0
    for c in lis:
        if ( c.Category in available ):
            count += 1
    return count
    
def format_date(date):
    try:
        temp = int(date[-4:])
        month, day, year = date.split("/")
        date = year
        date += "-"
        
        if ( len(month) == 1 ):
            date += "0"
        date += month
        date += "-"
        if ( len(day) == 1 ):
            date += "0"
        date += day
    except:
        temp = date
        date = "20"
        date += temp
    return date

def detail(request, id):
    # user must need to login to view pages
    if (not request.user.is_authenticated()):
        return redirect('/login')

    ticket = CallLog.objects.get(CallID = id)

    recvdDate = format_date(ticket.RecvdDate)

    #splitting the symptoms string into multiple fields for display
    temp = parsing(ticket.Symptoms, "|")

    if ( len(temp) <= 1 ):
        temp = parsing(ticket.Symptoms, "`")

    temp = get_data(temp)

    if ( ticket.Category == "Hardware" or
         ticket.Category == "Software" ):
        if ( ticket.Category == "Hardware" ):
            url = temp[5]
        else:
            url = temp[4]

        is_img = "false"

        #checking whether an image has been submitted
        if ( url[-4:] == ".png" or
             url[-4:] == ".jpg" or
             url[-4:] == ".gif" ):
             is_img = "img"
        elif ( len(url) > 1 and
               url[:4] == "http" ):
            is_img = "file"
        else:
            is_img = "Null"

    #designating fields for display based on the ticket's category
    if ( ticket.Category == "Hardware" ):
        equip = acceptable(temp[0])
        asset = acceptable(temp[1])
        device = acceptable(temp[2])
        description = acceptable(temp[3])
        error = acceptable(temp[4])

        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "Symptoms" : ticket.Symptoms,
            "RecvdDate" : recvdDate,
            "EquipType" : equip,
            "AssetTag" : asset,
            "DeviceName" : device,
            "Description" : description,
            "URL" : url,
            "is_img": is_img,
            "ErrorMsg" : error,
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority
        }

    elif ( ticket.Category == "Software" ):
        system = acceptable(temp[0])
        offline = acceptable(temp[1])
        description = acceptable(temp[2])
        replicate = acceptable(temp[3])

        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "RecvdDate" : recvdDate,
            "System" : system,
            "Offline" : offline,
            "Description" : description,
            "Replicate" : replicate,
            "URL" : url,
            "is_img": is_img,
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
    elif ( ticket.Category == "Service" ):
        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "RecvdDate" : recvdDate,
            "request_type" : temp[0],
            "System_type" : temp[1],
            "asset_tag" : temp[2],
            "move_location" : temp[3],
            "software" : temp[4],
            "pc" : temp[5],
            "description" : temp[6],
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority
        }
    elif ( ticket.Category == "Other" ):
        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "RecvdDate" : recvdDate,
            "System_type" : "NULL",
            "problem" : temp[0],
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority
        }

    else:
        context = {}

   # obtaining user's branch
    try:
        branch = UserProfile.objects.get(user=request.user).branch
    except:
        branch = "staff"
    context['branch'] = branch

    return render(request, 'epl/view-ticket.html', context)

# return the active username
def get_username(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

    return username

def get_branch(request, user):
    branch = None
    if request.user.is_authenticated():
        branch = user.userprofile.get_branch()

    return branch

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

    context = { "form" : form, "name" : "Sign In" }
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

# get a string if its acceptable
# i.e, len(string) > 0 then returns
# the string, otherwise nothing
def acceptable(string):
    if ( len(string) > 0 ):
        return string
    else:
        return ""

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

def successTicketSummary(request, id, pageSubmitType):
    ticket = CallLog.objects.get(CallID = id)

    recvdDate = format_date(ticket.RecvdDate)

    temp = parsing(ticket.Symptoms, "|")

    if ( len(temp) <= 1 ):
        temp = parsing(ticket.Symptoms, "`")

    if ( ticket.Category == "Hardware" ):
        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "Symptoms" : ticket.Symptoms,
            "RecvdDate" : recvdDate,
            "equipment_type" : temp[0],
            "asset_tag" : temp[1],
            "device_name" : temp[2],
            "problem_description" : temp[3],
            "error_messages" : temp[4],
            "image_url" : temp[5],
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority,
            "PageSubmitType" : pageSubmitType
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
            "Priority" : ticket.Priority,
            "PageSubmitType" : pageSubmitType
        }

    elif ( ticket.Category == "Software" ):
        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "RecvdDate" : recvdDate,
            "system" : temp[0],
            "system_offline" : temp[1],
            "problem_description" : temp[2],
            "steps_replicate_problem" : temp[3],
            "image_url" : temp[4],
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority,
            "PageSubmitType" : pageSubmitType
        }
    elif ( ticket.Category == "Service" ):
        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "RecvdDate" : recvdDate,
            "request_type" : temp[0],
            "System_type" : temp[1],
            "asset_tag" : temp[2],
            "move_location" : temp[3],
            "software" : temp[4],
            "pc" : temp[5],
            "description" : temp[6],
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority,
            "PageSubmitType" : pageSubmitType
        }
    elif ( ticket.Category == "Other" ):
        context = {
            "CallID" : ticket.CallID,
            "CustID" : ticket.CustID,
            "RecvdDate" : recvdDate,
            "problem" : temp[0],
            "Category" : ticket.Category,
            "CallStatus" : ticket.CallStatus,
            "Priority" : ticket.Priority,
            "PageSubmitType" : pageSubmitType
            }

    else:
        context = {}

    return context

#------------------------------------
# data saving for hardware tickets
#------------------------------------

# saving password data into database
def pass_database_saved(form, username, ticketID):
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
        if (ticketID == None):
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
        else:
           callLog_table = CallLog(
              CallID = ticketID,
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
def database_saved(form, username, ticketID):
    try:
        # getting data from the form
        asset_tag = form.cleaned_data.get("asset_tag")
        equipment_type = form.cleaned_data.get("equipment_type")
        problem_description = form.cleaned_data.get("problem_description")
        error_messages = form.cleaned_data.get("error_messages")
        file_upload = form.cleaned_data.get("file_upload")
        device_name = form.cleaned_data.get("device_name")
        image_url = form.cleaned_data.get("image_url")

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
        if (ticketID == None):
            callLog_table = CallLog(
            Symptoms = "|".join([callLog_Symptoms, image_url]), #adding the url of the image
            Priority = callLog_Priority,
            CallSource = callLog_CallSource,
            RecvdDate = callLog_RecvdDate,
            RecvdTime = callLog_RecvdTime,
            CustID = callLog_CustID,
            Tracker = callLog_Tracker,
            CallStatus = callLog_Status,
            Category = "Hardware"
            #get the value of image filed in hardware form and insert the the value to Image filed of CallLog model.
            )
        else:
            callLog_table = CallLog(
                CallID = ticketID,
            Symptoms = "|".join([callLog_Symptoms, image_url]), #adding the url of the image
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
            Description = "|".join([asgnmnt_Description, image_url]), # Abdullah adding the url of the image
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
def soft_database_saved(form, username, ticketID):
    try:
        # getting data from the form
        system = form.cleaned_data.get("system")
        system_offline = form.cleaned_data.get("system_offline")
        problem_description = form.cleaned_data.get("problem_description")
        steps_replicate_problem = form.cleaned_data.get("steps_replicate_problem")
        file_upload = form.cleaned_data.get("image_url")

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

        # description of problem
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += steps_replicate_problem
        asgnmnt_Description += steps_replicate_problem

        #image link
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"

        if ( file_upload == "" or
             file_upload == " " or
             file_upload == "http://" ):
            file_upload = "NULL"

        callLog_Symptoms += file_upload
        asgnmnt_Description += file_upload

        # priority
        if ( system_offline == "Yes" ):
            callLog_Priority = "1"
        else:
            callLog_Priority = "3"

        # call source
        callLog_CallSource = "Web"

        # assigned team name
        if( probType_ProbType == "Internet/Network" or probType_ProbType=="S:/ drive"):
            asgnmnt_TeamName = "Network Team"

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
        if (ticketID == None):
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
        else:
            callLog_table = CallLog(
                    CallID = ticketID,
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

# Save a service ticket
def service_database_saved(form, username, ticketID):
    try:
        # getting data from the form
        request_type = form.cleaned_data.get("request_type")
        system = form.cleaned_data.get("system")
        asset_tag = form.cleaned_data.get("asset_tag")
        move_location = form.cleaned_data.get("move_location")
        software = form.cleaned_data.get("software")
        pc = form.cleaned_data.get("pc")
        description = form.cleaned_data.get("description")

        # The service ticket doesn't require all the fields to be provided
        # By setting the value of the fields to 'Not Provided' in the database
        # it is misleading as we don't know if the user entered that, as well
        # the asset tag has a validation of having maximum of 5 characters
        # so setting it to 'Not Provided' breaks the form.
        #if ( len(system) < 1 ):
        #    system = "Not Provided"
        #if ( len(asset_tag) < 1 ):
        #    asset_tag = "Not Provided"
        #if ( len(move_location) < 1 ):
        #    move_location = "Not Provided"
        #if ( len(software) < 1 ):
        #    software = "Not Provided"
        #if ( len(pc) < 1 ):
        #    pc = "Not Provided"
        #if ( len(description) < 1 ):
        #    description = "Not Provided"

        # request type
        probType_ProbType = request_type
        callLog_Symptoms = request_type
        asgnmnt_Description = request_type

        # system type
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += system
        asgnmnt_Description += system


        # asset tag
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += asset_tag
        asgnmnt_Description += asset_tag


        # move location
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += move_location
        asgnmnt_Description += move_location

        # software
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += software
        asgnmnt_Description += software

        # pc
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += pc
        asgnmnt_Description += pc

        # description
        callLog_Symptoms += "|"
        asgnmnt_Description += "|"
        callLog_Symptoms += description
        asgnmnt_Description += description

        # priority
        callLog_Priority = "3"

        # call source
        callLog_CallSource = "Web"


        # assigned team name
        if( request_type == "Move equipment request"):
            asgnmnt_TeamName = "Project Team"
        else:
            asgnmnt_TeamName = "Administrative Team"

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

        if( request_type == "Move equipment request"):
            callLog_Status = "Needs Approval"
        else:
            callLog_Status = "Open"

        # CallLog Table
        if (ticketID == None):
            callLog_table = CallLog(
                    Symptoms = callLog_Symptoms,
                    Priority = callLog_Priority,
                    CallSource = callLog_CallSource,
                    RecvdDate = callLog_RecvdDate,
                    RecvdTime = callLog_RecvdTime,
                    CustID = callLog_CustID,
                    Tracker = callLog_Tracker,
                    CallStatus = callLog_Status,
                    Category = "Service"
            )
        else:
            callLog_table = CallLog(
                    CallID = ticketID,
                    Symptoms = callLog_Symptoms,
                    Priority = callLog_Priority,
                    CallSource = callLog_CallSource,
                    RecvdDate = callLog_RecvdDate,
                    RecvdTime = callLog_RecvdTime,
                    CustID = callLog_CustID,
                    Tracker = callLog_Tracker,
                    CallStatus = callLog_Status,
                    Category = "Service"
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
                ProbType= probType_ProbType
        )

        # Saving data into the database
        callLog_table.save()
        asgnmnt_table.save()
        probType_table.save()

        return "Ticket added sucessfully"

    except:
        return "Something went wrong"

# Save a general ticket
def general_database_saved(form, username, ticketID):
    try:
        # getting data from the form
        problem = form.cleaned_data.get("problem")

        # problem
        probType_ProbType = problem
        callLog_Symptoms = problem
        asgnmnt_Description = problem

        # priority
        callLog_Priority = "4"

        # call source
        callLog_CallSource = "Web"

        # assigned team name
        asgnmnt_TeamName = "NULL"

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
        if (ticketID == None):
            callLog_table = CallLog(
            Symptoms = callLog_Symptoms,
            Priority = callLog_Priority,
            CallSource = callLog_CallSource,
            RecvdDate = callLog_RecvdDate,
            RecvdTime = callLog_RecvdTime,
            CustID = callLog_CustID,
            Tracker = callLog_Tracker,
            CallStatus = callLog_Status,
            Category = "Other"
            )
        else:
            callLog_table = CallLog(
            CallID = ticketID,
            Symptoms = callLog_Symptoms,
            Priority = callLog_Priority,
            CallSource = callLog_CallSource,
            RecvdDate = callLog_RecvdDate,
            RecvdTime = callLog_RecvdTime,
            CustID = callLog_CustID,
            Tracker = callLog_Tracker,
            CallStatus = callLog_Status,
            Category = "Other"
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

def get_data(lis):
    new_list = []
    length = len(lis) - 1
    k = 0
    for i in range(0, 7):
        if ( i > length ):
            new_list.append("Not Provided")
        else:
            if ( lis[k] == "" or
                 lis[k] == "NULL" or
                 lis[k] == "N/A" ):
                new_list.append("Not Provided")
            else:
                new_list.append(lis[k])
            k += 1
    return new_list

@csrf_exempt
def alter_status(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        id = request.POST.get('id')

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
