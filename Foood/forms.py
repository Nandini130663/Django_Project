from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Foood.models import Exfd,Crpf,South

class Usregis(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["first_name","last_name","email","username"]
		widgets = {
		"first_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your First Name",
			"required":True,
			}),
		"last_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Last Name",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Emailid",
			"required":True,
			}),
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your UserName",
			"required":True,
			}),
		}

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class Upd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control","placeholder":'Enter your username'
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",'placeholder':'Enter your firstname'
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",'placeholder':'Enter your lastname'
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",'placeholder':'Enter your email'
			}),
		}

class Pad(forms.ModelForm):
	class Meta:
		model = Exfd
		fields = ["age","gender","impf","rollno","collegename"]
		widgets = {
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			}),
		"rollno":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your roll number",
			}),
		"collegename":forms.Select(attrs={
			"class":"form-control",
			}),
		}

class SoF(forms.ModelForm):
	class Meta:
		model = South
		fields = ["item","price","quantity","category"]
		widgets = {
		"item":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your item Name",
			"required":True,
			}),
		"price":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your UserName",
			"required":True,
			}),
		"quantity":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Last Name",
			"required":True,
			}),
		"category":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Emailid",
			"required":True,
			}),
		}

