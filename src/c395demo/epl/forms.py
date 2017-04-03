from django.utils.safestring import mark_safe
from epl.choices import *
from django import forms
from epl.models import *
from django.core.validators import RegexValidator

# import for user authentication
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )

class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if (username and password):
            user = authenticate(username=username, password=password)

            # if user not found in the database
            if (not user):
                raise forms.ValidationError("Error: either username or password is incorrect")

            # if user enters wrong password
            if (not user.check_password(password)):
                raise forms.ValidationError("Error: either username or password is incorrect")

            # User is no longer active
            if (not user.is_active):
                raise forms.ValidationError("User is no longer active")

        return super(UserLogin, self).clean(*args, **kwargs)

class HardwareTicketForm(forms.Form):
	asset_tag = forms.CharField(max_length=5, min_length=5,
	    validators=[RegexValidator(regex='^\d{5}$', message='Asset tag must be 5 integers', code='wrongInput')],
	    label=mark_safe('Asset Tag (<a href="/questions/whyname/" target="_blank">Where to find the Asset Tag</a>?)'))
	equipment_type = forms.ChoiceField(choices=EQUIPMENT_TYPE_CHOICES, widget=forms.Select(attrs={'id': 'id_equipment_type'}))
	problem_description = forms.CharField(widget=forms.Textarea)
	error_messages = forms.CharField(widget=forms.Textarea, required=False)
	image_url = forms.CharField(widget=forms.URLInput(attrs={'placeholder': 'https://'}), required=False)
	device_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'id_device_name'}), required=False)

class SoftwareTicketForm(forms.Form):
    system = forms.ChoiceField(choices=SOFTWARE_CHOICES,
        label='Which system?')
    system_offline = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_NO_CHOICE,
        label='Is the system completely offline/broken?')
    problem_description = forms.CharField(widget=forms.Textarea,
        label='Description of the Problem')
    steps_replicate_problem = forms.CharField(widget=forms.Textarea, required=False,
        label='Share any steps to replicate the problem')
    image_url = forms.CharField(widget=forms.URLInput(attrs={'placeholder': 'https://'}), required=False)
    # apply class to all fields.
    def __init__(self, *args, **kwargs):
        self.system = kwargs.pop('system',None)
        self.system_offline = kwargs.pop('system_offline',None)
        self.problem_description = kwargs.pop('problem_description',None)
        self.steps_replicate_problem = kwargs.pop('steps_replicate_problem',None)
        self.image_url = kwargs.pop('image_url',None)
        super(SoftwareTicketForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != "system_offline":
               self.fields[field].widget.attrs.update({'class' : 'software'})

class PasswordTicketForm(forms.Form):
    system_type = forms.ChoiceField(choices=SYSTEM_CHOICES)
    sys_user = forms.CharField(max_length=200)

class ServiceTicketForm(forms.Form):
    request_type = forms.ChoiceField(choices=REQUEST_TYPE_CHOICE, widget=forms.Select(attrs={'id': 'id_request_type'}) )
    system = forms.ChoiceField(choices=SYSTEM_CHOICES, widget=forms.Select(attrs={'id': 'id_system'}), required=False)
    asset_tag = forms.CharField(max_length=5, min_length=5, widget=forms.TextInput(attrs={'id': 'id_asset_tag'}),
		label=mark_safe('Asset Tag (<a href="/questions/whyname/" target="_blank">Where to find the Asset Tag</a>?) of the equipment you want moved or surplused'), required=False)
    move_location = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'id_move_location'}),
        label='Where would you like this equipment moved to?', required=False)
    software = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'id_software'}),
        label='What software are you looking for?', required=False)
    pc = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'id_pc'}),
        label='Which PC do you want this software installed on?', required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols': 10, 'id': 'id_description'}), max_length=500, required=False)
    def __init__(self, *args, **kwargs):
        self.request_type = kwargs.pop('request_type',None)
        self.system = kwargs.pop('system',None)
        self.asset_tag = kwargs.pop('asset_tag',None)
        self.move_location = kwargs.pop('move_location',None)
        self.software = kwargs.pop('software',None)
        self.pc = kwargs.pop('pc',None)
        self.description = kwargs.pop('description',None)
        super(ServiceTicketForm, self).__init__(*args, **kwargs)


class GeneralTicketForm(forms.Form):
    problem = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 10}), max_length=500)
    def __init__(self, *args, **kwargs):
        self.problem = kwargs.pop('problem',None)
        super(GeneralTicketForm, self).__init__(*args, **kwargs)

