from django import forms
from django.contrib.auth.models import User #django nte user model import cheyan

class HireRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)#hiddenpassword #widget refers to an interface element which is used to interact with a users using the datatype
    cpassword=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    email=forms.EmailField(required=True)
    phone=forms.IntegerField(label='Phone',widget=forms.TextInput(attrs={'placeholder':''}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','phone','password','cpassword']