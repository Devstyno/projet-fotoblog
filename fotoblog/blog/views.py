from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.forms import PhotoForm
from blog.models import Photo

# Create your views here.
@login_required
def accueil(request):
    photos = Photo.objects.all()
    context = {"photos" : photos}
    return render(request, 'blog/accueil.html', context)

@login_required
def photo_upload(request):
    form = PhotoForm()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False) # creer un objet du model
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can
            photo.save() # enregistrer l'objet dans la bdd
            return redirect("accueil")

    return render(request, "blog/photo_upload.html", {"form" : form})

def contact_us(request):
    return render(request, 'blog/contact_us.html')