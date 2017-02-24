from django import forms
from django.utils.safestring import mark_safe
from epl.choices import *

class HardwareTicketForm(forms.Form):
	asset_tag = forms.CharField(max_length=200,
		label=mark_safe('Asset Tag (<a href="/questions/whyname/" target="_blank">Where to find the Asset Tag</a>?)'))
	equipment_type = forms.ChoiceField(choices=EQUIPMENT_TYPE_CHOICES,initial=NONE)
	problem_description = forms.CharField(widget=forms.Textarea)
	error_messages = forms.CharField(widget=forms.Textarea)
	file_upload = forms.FileField(required=False)
	device_name = forms.CharField(max_length=200, required=False)
	
class SoftwareTicketForm(forms.Form):
	system = forms.ChoiceField(choices=SOFTWARE_CHOICES,
		label='Which system?')
	system_offline = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_NO_CHOICE, required=False,
		label='Is the system completely offline/broken?')
	problem_description = forms.CharField(widget=forms.Textarea,
		label='Description of the Problem')
	steps_replicate_problem = forms.CharField(widget=forms.Textarea,
		label='Share any steps to replicate the problem')
	file_upload = forms.FileField(required=False)