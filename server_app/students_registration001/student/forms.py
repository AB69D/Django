from django import forms

class studentregistration(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter Your Name'})
    email =  forms.EmailField(error_messages={'required':'Enter Your Email'}) 
    password1 = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter Your Password'})
    password2 = forms.CharField(label= 'password(again)',widget=forms.PasswordInput)
    
    
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname)<4:
    #         raise forms.ValidationError('Ensure name is more then 4 char ')
    #     return valname 
    def clean(self):
        cleaned_data =  super().clean() # apply all  validation of parent class  
        # valname = self.cleaned_data['name']
        # valemail  = self.cleaned_data['email']
        # if len(valname)<4:
        #     raise forms.ValidationError('Ensure name is more then 4 char ')
        
        # if len(valemail)<10:
        #     raise forms.ValidationError('Ensure email is more then 10 char ')
        valpass = self.cleaned_data['password1']
        valconpass = self.cleaned_data['password2']
        if(valpass!= valconpass):
            raise forms.ValidationError('Password are not same ')