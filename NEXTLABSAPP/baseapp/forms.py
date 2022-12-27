from django import forms
from .models import Users
class usersignupform(forms.ModelForm):
    class Meta:
        model=Users
        fields=["username","password","email"]
class userloginform(forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(max_length=10)