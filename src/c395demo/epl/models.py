from django.db import models
from epl.choices import *

# Create your models here.

class CallLog(models.Model):
    CallID = models.CharField(max_length=8,default='NULL')
    CustID = models.CharField(max_length=50,default='NULL')
    CustType = models.CharField(max_length=50,default='NULL')
    CallType = models.CharField(max_length=100,default='NULL')
    Tracker = models.CharField(max_length=96,default='NULL')
    CallStatus = models.CharField(max_length=50,default='NULL')
    Severity = models.IntegerField(default=0)
    CDuration = models.DecimalField(max_digits=9, decimal_places=4, default=0)
    CallCount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    StopWatch = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    ClosedBy = models.CharField(max_length=96,default='NULL')
    ClosedDate = models.CharField(max_length=10,default='NULL')
    ClosedTime = models.CharField(max_length=8,default='NULL')
    Symptoms = models.TextField(default='NULL')
    CallResolution = models.TextField(default='NULL')
    RecvdBy = models.CharField(max_length=96,default='NULL')
    RecvdDate = models.CharField(max_length=10,default='NULL')
    RecvdTime = models.CharField(max_length=8,default='NULL')
    ModBy = models.CharField(max_length=96,default='NULL')
    ModDate = models.CharField(max_length=10,default='NULL')
    ModTime = models.CharField(max_length=8,default='NULL')
    DTLastMod = models.IntegerField(default=0)
    CallSource = models.CharField(max_length=15,default='NULL')
    Category = models.CharField(max_length=20,default='NULL')
    TotalAsgnmntTime = models.IntegerField(default=0)
    CatHeading = models.CharField(max_length=25,default='NULL')
    TotalJournalTime = models.IntegerField(default=0)
    TotalTime = models.IntegerField(default=0)
    SL_Callback_Target = models.IntegerField(default=0)
    SL_Callback_Date = models.CharField(max_length=10,default='NULL')
    SL_Callback_Time = models.CharField(max_length=8,default='NULL')
    SL_Resolution_Target = models.IntegerField(default=0)
    SL_Resolution_Date = models.CharField(max_length=10,default='NULL')
    SL_Resolution_Time = models.CharField(max_length=8,default='NULL')
    SL_Clock_Status = models.CharField(max_length=20,default='NULL')
    SL_Button_Status = models.CharField(max_length=20,default='NULL')
    FirstResolution = models.CharField(max_length=3,default='NULL')
    SL_Complete_Status = models.CharField(max_length=25,default='NULL')
    ProblemDesc = models.TextField(default='NULL')
    ProbType = models.CharField(max_length=50,default='NULL')
    SevChanged = models.CharField(max_length=2,default='NULL')
    Hostname = models.CharField(max_length=20,default='NULL')
    Yes_No = models.CharField(max_length=1,default='NULL')
    TimeSpent = models.IntegerField(default=0)
    Priority = models.CharField(max_length=2,default='NULL')
    Dueby = models.CharField(max_length=10,default='NULL')
    PastDue = models.CharField(max_length=10,default='NULL')
    SaveFlag = models.CharField(max_length=5,default='NULL')
    TempTime = models.IntegerField(default=0)
    
class HardwareTicket(models.Model):
	asset_id = models.CharField(max_length=200)
	equipment_type = models.CharField(
		max_length=3,
		choices=EQUIPMENT_TYPE_CHOICES,
		default=NONE)
	problem_description = models.TextField(max_length=500, default=' ')
	error_messages = models.CharField(max_length=500,blank=True)
	file_upload = models.BinaryField(blank=True)
	device_name = models.CharField(max_length=200,blank=True)
	
class SoftwareTicket(models.Model):
	system = models.CharField(choices=SOFTWARE_CHOICES,
		default=NONE,
		max_length=200)
	system_offline = models.CharField(choices=YES_NO_CHOICE, max_length=1)
	problem_description = models.CharField(max_length=500)
	steps_replicate_problem = models.CharField(max_length=500)
	file_upload = models.BinaryField()
