from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm

# Create your views here.
def login_page(request):
    form = LoginForm()
    message = ''

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                redirect("accueil")
            else:
                message = "Identifiants invalides."
    
    context = {"form" : form, "message" : message}
    
    return render(request, 'authentication/login.html', context)

def logout_user(request):
    logout(request)
    return redirect("login")