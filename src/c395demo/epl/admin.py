from django.contrib import admin

# Register your models here.

from epl.models import CallLog, Asgnmnt, ProbType

admin.site.register(CallLog)
admin.site.register(Asgnmnt)
admin.site.register(ProbType)
