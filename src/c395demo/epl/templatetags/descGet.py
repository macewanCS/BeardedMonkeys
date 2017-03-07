from django import template
from epl.models import CallLog

register = template.Library()

@register.simple_tag
def descGet(id):
    ticket = CallLog.objects.get(CallID = id)
    temp = ticket.Symptoms.split("`")
    if (ticket.Category == "Hardware"):
        return temp[3][:15]
    elif (ticke.Category == "Software"):
        return temp[2][:15]
