from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def accueil(request):
    return render(request, 'blog/accueil.html')

def contact_us(request):
    return render(request, 'blog/contact_us.html')