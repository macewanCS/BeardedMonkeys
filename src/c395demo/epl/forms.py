
from django.utils.safestring import mark_safe
from epl.choices import *
from django import forms

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
	asset_tag = forms.CharField(max_length=200,
		label=mark_safe('Asset Tag (<a href="/questions/whyname/" target="_blank">Where to find the Asset Tag</a>?)'))
	equipment_type = forms.ChoiceField(choices=EQUIPMENT_TYPE_CHOICES)
	problem_description = forms.CharField(widget=forms.Textarea)
	error_messages = forms.CharField(widget=forms.Textarea, required=False)
	file_upload = forms.FileField(required=False)
	device_name = forms.CharField(max_length=200, required=False)

class SoftwareTicketForm(forms.Form):
	system = forms.ChoiceField(choices=SOFTWARE_CHOICES,
		label='Which system?')
	system_offline = forms.ChoiceField(widget=forms.RadioSelect, choices=YES_NO_CHOICE,
		label='Is the system completely offline/broken?')
	problem_description = forms.CharField(widget=forms.Textarea,
		label='Description of the Problem')
	steps_replicate_problem = forms.CharField(widget=forms.Textarea, required=False,
		label='Share any steps to replicate the problem')
	file_upload = forms.FileField(required=False)

