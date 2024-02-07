from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.forms import formset_factory
from blog.forms import PhotoForm, BlogForm, DeleteBlogForm, FollowUsersForm
from blog.models import Photo, Blog

# Create your views here.
@login_required
def accueil(request):
    blogs = Blog.objects.all()
    photos = Photo.objects.all()
    context = {
        "photos" : photos,
        "blogs" : blogs
    }
    return render(request, 'blog/accueil.html', context)

@login_required
@permission_required('blog.add_photo', raise_exception=True)
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

@login_required
@permission_required('blog.add_photo', raise_exception=True)
def create_multiple_photos(request):
    PhotoFormSet = formset_factory(PhotoForm, extra=5)
    formset = PhotoFormSet()
    if request.method == "POST":
        formset = PhotoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.uploader = request.user
                    photo.save()
            return redirect("accueil")
    context = {"formset" : formset}
    return render(request, "blog/create_multiple_photos.html", context)

@login_required
@permission_required(['blog.add_photo', 'blog.add_blog'], raise_exception=True)
def blog_creation(request):
    blog_form = BlogForm()
    photo_form = PhotoForm()
    if request.method == "POST":
        blog_form = BlogForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.photo = photo
            blog.author = request.user
            blog.save()
            return redirect("accueil")
    context = {
        "blog_form" : blog_form,
        "photo_form" : photo_form
    }
    return render(request, "blog/blog_creation.html", context)

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {"blog" : blog}
    return render(request, "blog/blog_reading.html", context)

@login_required
@permission_required('blog.change_blog', raise_exception=True)
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    edit_form = BlogForm(instance=blog)
    delete_form = DeleteBlogForm()
    if request.method == 'POST':
        if "edit_blog" in request.POST:
            edit_form = BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect("accueil")
        elif "delete_blog" in request.POST:
            delete_form = DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect("accueil")
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'blog/edit_blog.html', context)

def contact_us(request):
    return render(request, 'blog/contact_us.html')

def about_us(request):
    return render(request, 'blog/a_propos.html')

@login_required
def follow_users(request):
    form = FollowUsersForm(instance=request.user)
    if request.method == "POST":
        form = FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accueil")

    path = "blog/follow_users_form.html"
    context = {"form" : form}

    return render(request, path, context)