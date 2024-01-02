from django import forms
from .models import UserAccount

class UserAccountForm(forms.ModelForm):
    class Meta:
        model=UserAccount
        fields=("__all__")
        widgets = {
                'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'UserName'
                }),
                'password': forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                }),
                'firstname': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
                'lastname': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
                'mobile': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Mobile'
                }),
                }


from django import forms
from .models import HiddenImage
from django import forms

class HiddenImageForm(forms.Form):
  text = forms.CharField(max_length=1024)
  image = forms.FileField()
