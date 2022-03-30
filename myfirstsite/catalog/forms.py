
from django import forms
from .models import Image



class TaskForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    complexity = forms.DecimalField(label='Complexity', max_digits=10, decimal_places=2)
    options = forms.IntegerField(label="Options")
    description = forms.CharField(label="Description", widget=forms.Textarea)


class EditTaskDescriptionForm(forms.Form):
   description = forms.CharField(label="Description", widget=forms.Textarea)


class ReviewForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)



class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')