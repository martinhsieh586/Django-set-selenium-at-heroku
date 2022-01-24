from django import forms

class UserForm(forms.Form):
    username=forms.CharField(max_length=20)
    useremail=forms.EmailField(max_length=100)
    userpassword=forms.CharField(max_length=20)
class LoginForm(forms.Form):
    useremail=forms.EmailField(max_length=100)
    userpassword=forms.CharField(max_length=20)   