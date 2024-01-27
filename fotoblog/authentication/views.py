from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm
from django.views.generic import View

# Create your views here.

class LoginPageView(View):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form" : form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("accueil")
            message = "Identifiants invalides !"
        return render(request, self.template_name, {"form" : form, "message" : message})

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
                return redirect("accueil")
            else:
                message = "Identifiants invalides."
    
    context = {"form" : form, "message" : message}
    
    return render(request, 'authentication/login.html', context)

def logout_user(request):
    logout(request)
    return redirect("login")