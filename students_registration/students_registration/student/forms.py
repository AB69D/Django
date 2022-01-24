from django import forms

class studentregistration(forms.Form):
    name = forms.CharField()
    email =  forms.EmailField() 