# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hardware',
            old_name='name',
            new_name='DTLastMod',
        ),
        migrations.RenameField(
            model_name='hardware',
            old_name='number',
            new_name='SL_Callback_Target',
        ),
        migrations.AddField(
            model_name='hardware',
            name='CDuration',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='hardware',
            name='CallCount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='hardware',
            name='CallID',
            field=models.CharField(default='NULL', max_length=8),
        ),
        migrations.AddField(
            model_name='hardware',
            name='CallResolution',
            field=models.TextField(default='NULL'),
        ),
        migrations.AddField(
            model_name='hardware',
            name='CallSource',
            field=models.CharField(default='NULL', max_length=15),
        ),
        migrations.AddField(
            model_name='hardware',
            name='CallStatus',
            field=models.CharField(default='NULL', max_length=50),
        ),
        migrations.AddField(
            model_name='hardware',
            name='CallType',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='hardware',
            name='CatHeading',
            field=models.CharField(default='NULL', max_length=25),
        ),
        migrations.AddField(
            model_name='hardware',
            name='Category',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='hardware',
            name='ClosedBy',
            field=models.CharField(default='NULL', max_length=96),
        ),
        migrations.AddField(
            model_name='hardware',
            name='ClosedDate',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AddField(
            model_name='hardware',
            name='ClosedTime',
            field=models.CharField(default='NULL', max_length=8),
        ),
        migrations.AddField(
            model_name='hardware',
            name='CustID',
            field=models.CharField(default='NULL', max_length=50),
        ),
        migrations.AddField(
            model_name='hardware',
            name='CustType',
            field=models.CharField(default='NULL', max_length=50),
        ),
        migrations.AddField(
            model_name='hardware',
            name='Dueby',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AddField(
            model_name='hardware',
            name='FirstResolution',
            field=models.CharField(default='NULL', max_length=3),
        ),
        migrations.AddField(
            model_name='hardware',
            name='Hostname',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='hardware',
            name='ModBy',
            field=models.CharField(default='NULL', max_length=96),
        ),
        migrations.AddField(
            model_name='hardware',
            name='ModDate',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AddField(
            model_name='hardware',
            name='ModTime',
            field=models.CharField(default='NULL', max_length=8),
        ),
        migrations.AddField(
            model_name='hardware',
            name='PastDue',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AddField(
            model_name='hardware',
            name='Priority',
            field=models.CharField(default='NULL', max_length=2),
        ),
        migrations.AddField(
            model_name='hardware',
            name='ProbType',
            field=models.CharField(default='NULL', max_length=50),
        ),
        migrations.AddField(
            model_name='hardware',
            name='ProblemDesc',
            field=models.TextField(default='NULL'),
        ),
        migrations.AddField(
            model_name='hardware',
            name='RecvdBy',
            field=models.CharField(default='NULL', max_length=96),
        ),
        migrations.AddField(
            model_name='hardware',
            name='RecvdDate',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AddField(
            model_name='hardware',
            name='RecvdTime',
            field=models.CharField(default='NULL', max_length=8),
        ),
        migrations.AddField(
            model_name='hardware',
            name='SL_Button_Status',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='hardware',
            name='SL_Callback_Date',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AddField(
            model_name='hardware',
            name='SL_Callback_Time',
            field=models.CharField(default='NULL', max_length=8),
        ),
        migrations.AddField(
            model_name='hardware',
            name='SL_Clock_Status',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AddField(
            model_name='hardware',
            name='SL_Complete_Status',
            field=models.CharField(default='NULL', max_length=25),
        ),
        migrations.AddField(
            model_name='hardware',
            name='SL_Resolution_Date',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AddField(
            model_name='hardware',
            name='SL_Resolution_Target',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hardware',
            name='SL_Resolution_Time',
            field=models.CharField(default='NULL', max_length=8),
        ),
        migrations.AddField(
            model_name='hardware',
            name='SaveFlag',
            field=models.CharField(default='NULL', max_length=5),
        ),
        migrations.AddField(
            model_name='hardware',
            name='SevChanged',
            field=models.CharField(default='NULL', max_length=2),
        ),
        migrations.AddField(
            model_name='hardware',
            name='Severity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hardware',
            name='StopWatch',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='hardware',
            name='Symptoms',
            field=models.TextField(default='NULL'),
        ),
        migrations.AddField(
            model_name='hardware',
            name='TempTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hardware',
            name='TimeSpent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hardware',
            name='TotalAsgnmntTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hardware',
            name='TotalJournalTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hardware',
            name='TotalTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hardware',
            name='Tracker',
            field=models.CharField(default='NULL', max_length=96),
        ),
        migrations.AddField(
            model_name='hardware',
            name='Yes_No',
            field=models.CharField(default='NULL', max_length=1),
        ),
    ]
