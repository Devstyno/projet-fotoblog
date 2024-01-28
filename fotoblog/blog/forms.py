from blog.models import Photo, Blog
from django.forms import ModelForm

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ("image", "caption")

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "content")