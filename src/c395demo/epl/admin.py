from django.contrib import admin

# Register your models here.

from epl.models import CallLog
from epl.models import HardwareTicket, SoftwareTicket
admin.site.register(CallLog)
admin.site.register(HardwareTicket)
admin.site.register(SoftwareTicket)
