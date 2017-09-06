from django import forms
from django.contrib.auth.forms import AuthenticationForm
# from .models import Pessoas

class LoginForm(AuthenticationForm):
	username = forms.CharField(max_length=255)
	password = forms.CharField(max_length=255)


# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = Pessoas
# 		fields = ['matricula', 'nome', 'email', 'rfid']
