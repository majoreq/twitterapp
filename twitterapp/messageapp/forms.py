from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=128, label='login')
    password = forms.CharField(max_length=128, label='password', widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=128, label='username')
    email = forms.EmailField(label='email')
    password = forms.CharField(max_length=128, label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=128, label='wpisz ponownie hasło', widget=forms.PasswordInput)