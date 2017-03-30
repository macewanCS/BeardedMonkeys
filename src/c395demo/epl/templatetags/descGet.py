from django import template
from epl.models import CallLog

register = template.Library()

@register.filter(name='firstUpper')
def firstUpper(string):
    return string.upper()
    
@register.filter(name='get_date')
def get_date(string):
    try:
        temp = int(string[-4:])
        month, day, year = string.split("/")
        string = year
        string += "-"
        if ( len(month) == 1 ):
            string += "0"
        string += month
        string += "-"
        if ( len(day) == 1 ):
            string += "0"
        string += day
    except:
        temp = string
        string = "20"
        string += temp
    return string

@register.simple_tag
def descGet(id):
    ticket = CallLog.objects.get(CallID = id)
    temp = ticket.Symptoms.split("|")
    #obtain description from symptoms string
    if ( len(temp) <= 1 ):
        temp = ticket.Symptoms.split("`")
    
    string = ""
    if (ticket.Category == "Hardware"):
        if ( not len(temp) >= 4 ):
            return truncate(temp[0])
        return truncate(temp[3])
        
    elif (ticket.Category == "Software"):
        if ( not len(temp) >= 3 ):
            return truncate(temp[0])
        return truncate(temp[2])
        
    elif (ticket.Category == "Service"):
        return truncate(temp[0])
    #password tickets don't have descriptions; display special message instead    
    elif (ticket.Category == "Password"):
        string += "Reset "
        string += temp[0]
        string += " password."
        return string
        
    elif (ticket.Category == "Other"):
        return truncate(temp[0])
#ensure description isn't too long to properly display in view pages        
def truncate(string):
    if (len(string) > 30):
        string = string[:30]
        string += "..."
    return string
    
