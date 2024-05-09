from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todo.models import Project,Todo



class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        
        
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))  
    


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=["title",]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title'}),
        }
        
class TodoForm(forms.ModelForm):
     class Meta:
        model=Todo     
        fields=['name','description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project title'}),

        }