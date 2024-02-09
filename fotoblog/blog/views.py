from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.forms import formset_factory
from django.db.models import Q
from blog.forms import PhotoForm, BlogForm, DeleteBlogForm, FollowUsersForm
from blog.models import Photo, Blog

# Create your views here.
@login_required
def accueil(request):
    blogs = Blog.objects.filter(
        Q(contributors__in=request.user.follows.all()) | Q(starred=True)
    )
    photos = Photo.objects.filter(
        uploader__in=request.user.follows.all()
    ).exclude(
        blog__in=blogs
    )

    blogs_and_photos = sorted(
        chain(blogs, photos),
        key=lambda instance: instance.date_created,
        reverse=True
    )

    paginator = Paginator(blogs_and_photos, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    path = "blog/accueil.html"
    context = {
        "page_obj" : page_obj
    }
    
    return render(request, path, context)

@login_required
def photo_feed(request):
    photos = Photo.objects.all().filter(
        Q(uploader__in=request.user.follows.all())
    )
    photos = photos.order_by("-date_created") # le - permet de renverser l'ordre par defaut de la sequence

    paginator = Paginator(photos, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    path = "blog/photo_feed.html"
    context = {"page_obj" : page_obj}
    
    return render(request, path, context)

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
            blog.contributors.add(request.user, through_defaults={'contribution' : 'Auteur principal'})
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