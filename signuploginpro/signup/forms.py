from django import forms
from .models import SignupData
class RegistrationForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }
        )
    )
    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter user name'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter user email'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm pwd',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter conform password'
            }
        )
    )
    mobile = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter mobile number'
            }
        )
    )



    def clean_username(self):
        username = self.cleaned_data.get('username')

        qs = SignupData.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("User name is taken already.")
        elif len(username)<=5:
            raise forms.ValidationError("User Name Must have more then 5 Chars")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = SignupData.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email name is taken already.")
        elif not 'gmail.com' in email:
            raise forms.ValidationError("Email has to end with gmail.com")
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        mob = SignupData.objects.filter(mobile=mobile)
        if mob.exists():
            raise  forms.ValidationError('Mobile Number Already Taken')
        elif len(str(mobile)) != 10:
            raise forms.ValidationError('Enter Valid Mobile Number')
        return mobile

    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password2 != password1 :
            raise forms.ValidationError("Passwords must match.")
        elif len(password1) <= 4 or len(password1) >= 15:
             raise forms.ValidationError("Password length must be more then 4 chars or less then 15")
        return data
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter user name'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }
        )
    )