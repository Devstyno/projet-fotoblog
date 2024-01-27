from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, RegisteringForm
from django.views.generic import View
from django.conf import settings
from authentication.models import User

# Create your views here.
class RegisteringPageView(View):
    form_class = RegisteringForm
    template_name = "authentication/inscription.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form" : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # User.objects.create_user(
            #     username = form.cleaned_data["username"],
            #     password = form.cleaned_data["password"],
            #     role = form.cleaned_data["role"]
            # )
            user = form.save()
            # auto login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, self.template_name, {"form" : form})

def registering_page(request):
    form = RegisteringForm()
    if request.method == "POST":
        form = RegisteringForm(request.POST)
        if form.is_valid():
            # User.objects.create_user(
            #     username = form.cleaned_data["username"],
            #     password = form.cleaned_data["password"],
            #     role = form.cleaned_data["role"]
            # )
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    context = {"form" : form}
    return render(request, "authentication/inscription.html", context)

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