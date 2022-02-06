from django import forms
from .models import student


class studentregistration(forms.ModelForm):
    class Meta:
        model = student
        fields =['name','email','password']
        labels = {'name':'Enter Your Name', 'email':'Enter Your Email','password':'Enter Your Password'}
        help_text = {'name':'Should be 20 character'}
        error_messages = {'name':{'required':'You must have enter your name'},
                          'password':{'required':'Please enter your password'}}
        widgets = {'password':forms.PasswordInput,
                   'name':forms.TextInput(attrs={'class':'myclass'})}