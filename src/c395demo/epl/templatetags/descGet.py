from django import template
from epl.models import CallLog

register = template.Library()

@register.simple_tag
def descGet(id):
    ticket = CallLog.objects.get(CallID = id)
    temp = ticket.Symptoms.split("|")
    
    string = ""
    if (ticket.Category == "Hardware"):
        string += temp[3]
        if (len(string) > 15):
            string = temp[3][:20]
            string += "..."
        return string
    elif (ticket.Category == "Software"):
        string += temp[2]
        if (len(string) > 15):
            string = temp[2][:20]
            string += "..."
        return string
