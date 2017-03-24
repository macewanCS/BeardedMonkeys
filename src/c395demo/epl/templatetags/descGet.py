from django import template
from epl.models import CallLog

register = template.Library()

@register.filter(name='firstUpper')
def firstUpper(string):
    return string.upper()

@register.simple_tag
def descGet(id):
    ticket = CallLog.objects.get(CallID = id)
    temp = ticket.Symptoms.split("|")
    if ( len(temp) <= 1 ):
        temp = ticket.Symptoms.split("`")
    
    string = ""
    if (ticket.Category == "Hardware"):
        string += temp[3]
        if (len(string) > 20):
            string = temp[3][:20]
            string += "..."
        return string
    elif (ticket.Category == "Software"):
        string += temp[2]
        if (len(string) > 20):
            string = temp[2][:20]
            string += "..."
        return string
    elif (ticket.Category == "Service"):
        #for when description field is implemented
        #if (temp[6]):
        #    string += temp[6]
        #    if (len(string) > 20):
        #        string = temp[6][:20]
        #        string += "..."
        #else:
        string = "Description field not yet implemented."
        return string
    elif (ticket.Category == "Password"):
        string += "Reset "
        string += temp[0]
        string += " password."
        return string
    elif (ticket.Category == "Other"):
        string += temp[0]
        if (len(string) > 20):
            string = temp[0][:20]
            string += "..."
        return string
