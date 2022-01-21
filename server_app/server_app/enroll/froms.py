from django import forms

class studentregistration(forms.Form):
    student_Id = forms.IntegerField()
    name = forms.CharField()
    email = forms.EmailField()
    key = forms.CharField(widget=forms.HiddenInput)
    
    