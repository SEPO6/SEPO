from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label = "username",max_length = 12)
	password = forms.CharField(label = "password",max_length = 20, widget=forms.PasswordInput())

class JoinForm(forms.Form):
	username = forms.CharField(label = "USERNAME",min_length=4, max_length = 12, required=True)
	password = forms.CharField(label = "PASSWORD", min_length = 6, max_length = 20, required=True, widget=forms.PasswordInput)
	password_check = forms.CharField(label = "PASSWORD(again)",min_length = 6, max_length = 20, required=True, widget=forms.PasswordInput)
