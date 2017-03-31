from django import template

register = template.Library()

@register.simple_tag
def editURL(ticketType, ticketID):
    if (ticketType == "Other"):
        return "/general?ticketID=" + str(ticketID)
    elif (ticketType == "Password"):
        return "/password-recovery?ticketID=" + str(ticketID)
    elif (ticketType == "Service"):
        return "/service-request?ticketID=" + str(ticketID)
    elif (ticketType == "Software"):
        return "/software?ticketID=" + str(ticketID)
    elif (ticketType == "Hardware"):
        return "/hardware?ticketID=" + str(ticketID)
    else:
       return "/"
