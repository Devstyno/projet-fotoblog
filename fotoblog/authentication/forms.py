from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class RegisteringForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # Nous utilisons également la méthode utilitaire  get_user_model,
        # qui vous permet d’obtenir le modèle  User sans l’importer directement.
        # C’est particulièrement important si vous construisez une application conçue pour être réutilisée
        # dans différents projets.
        fields = ("username", "email", "first_name", "last_name", "role")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Nom d'utilisateur")
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label="Mot de passe")

class UploadProfilePhotoForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("profile_photo", )