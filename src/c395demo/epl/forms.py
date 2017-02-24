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
                raise forms.ValidationError("Sorry, the username not exist")
            
            # if user enters wrong password
            if (not user.check_password(password)):
                raise forms.ValidationError("Incorrect Password")
                
            # User is no longer active
            if (not user.is_active):
                raise forms.ValidationError("User is no longer active")
            
        return super(UserLogin, self).clean(*args, **kwargs)
            
            
