from django import forms
from authentication.models import User

class RegisteringForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        # exclude = ()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Nom d'utilisateur")
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label="Mot de passe")