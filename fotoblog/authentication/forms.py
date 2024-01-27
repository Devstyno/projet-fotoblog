from django import forms
from authentication.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class RegisteringForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model() # Nous utilisons également la méthode utilitaire  get_user_model, qui vous permet d’obtenir le modèle  Usersans l’importer directement. C’est particulièrement important si vous construisez une application conçue pour être réutilisée dans différents projets.
        fields = ("username", "email", "first_name", "last_name", "role")

# class RegisteringForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"
#         # exclude = ()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Nom d'utilisateur")
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label="Mot de passe")