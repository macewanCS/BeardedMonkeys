from django.db import models
from django.contrib.auth.models import User
from epl.choices import *

# Create your models here.

class CallLog(models.Model):
    CallID = models.AutoField(primary_key=True)
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
    FirstResolution = models.CharField(max_length=3,default='NIL')
    SL_Complete_Status = models.CharField(max_length=25,default='NULL')
    ProblemDesc = models.TextField(default='NULL')
    ProbType = models.CharField(max_length=50,default='NULL')
    SevChanged = models.CharField(max_length=2,default='NL')
    Hostname = models.CharField(max_length=20,default='NULL')
    Yes_No = models.CharField(max_length=1,default='N')
    TimeSpent = models.IntegerField(default=0)
    Priority = models.CharField(max_length=2,default='NL')
    Dueby = models.CharField(max_length=10,default='NULL')
    PastDue = models.CharField(max_length=10,default='NULL')
    SaveFlag = models.CharField(max_length=5,default='NULL')
    TempTime = models.IntegerField(default=0)
    
class Asgnmnt (models.Model):
    AssignedBy= models.CharField(max_length=96,default='NULL')
    DateAssign= models.CharField(max_length=10,default='NULL')
    TimeAssign = models.CharField(max_length=8,default='NULL')
    Assignee= models.CharField(max_length=96,default='NULL')
    Description = models.TextField(default='NULL')
    DateAcknow = models.CharField(max_length=10,default='NULL')
    TimeAcknow = models.CharField(max_length=8,default='NULL')
    DateResolv = models.CharField(max_length=10,default='NULL')
    TimeResolv = models.CharField(max_length=8,default='NULL')
    Resolution = models.TextField(default='NULL')
    CallID = models.CharField(max_length=8,default='NULL')
    HEATSeq = models.IntegerField(default=0)
    EMail = models.CharField(max_length=100,default='NULL')
    DTLastMod = models.IntegerField(default=0)
    WhoAcknow = models.CharField(max_length=96,default='NULL')
    WhoResolv = models.CharField(max_length=96,default='NULL')
    TargetTime = models.CharField(max_length=8,default='NULL')
    TargetDate = models.CharField(max_length=10,default='NULL')
    SLAResTime = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    TotalAsgnmntTime = models.IntegerField(default=0)
    CallType = models.CharField(max_length=100,default='NULL')
    ResolveOrder = models.IntegerField(default=0)
    Status = models.CharField(max_length=25,default='NULL')
    ModBy = models.CharField(max_length=50,default='NULL')
    ModDate = models.CharField(max_length=10,default='NULL')
    ModTime = models.CharField(max_length=8,default='NULL')
    TimeUpdate = models.IntegerField(default=0)
    TeamName = models.CharField(max_length=30,default='NULL')
    TempNotes = models.TextField(default='NULL')
    TempTime= models.IntegerField(default=0)
   
class ProbType(models.Model):
    ProbType = models.CharField(max_length=25,default='NULL')
    Description = models.TextField(default='NULL')
    Category = models.CharField(max_length=20,default='NULL')
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    status = models.CharField(max_length=20,default='staff')
    branch = models.CharField(max_length=20,default='home')

    def __unicode__(self):
        return self.user.username
        
    def __str__(self):
        return self.user.username
        
    def get_branch(self):
        return self.branch
        
    def get_status(self):
        return self.status
    
