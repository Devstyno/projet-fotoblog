"""
URL configuration for fotoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication import views as av # av for authenticationviews
from blog import views as bv # bv for blogviews
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', av.registering_page, name="register"),
    # path('register/', av.RegisteringPageView.as_view(), name="register"),
    # path('', av.LoginPageView.as_view(), name="login"),
    path('logout/', av.logout_user, name="logout"),
    path(
        '',
        LoginView.as_view(
            template_name = "authentication/login.html",
            redirect_authenticated_user = True
        ),
        name="login"
    ),
    # path('logout/', LogoutView.as_view(), name="logout"),
    path(
        'password/change/',
        PasswordChangeView.as_view(
            template_name = "authentication/password_update.html"
        ),
        name="password_change"
    ),
    path(
        'password/change/done/',
        PasswordChangeDoneView.as_view(
            template_name = "authentication/password_change_done.html"
        ),
        name="password_change_done"
    ),
    path('accueil/', bv.accueil, name="accueil"),
    path('contact-us/', bv.contact_us, name="contact_us")
]
