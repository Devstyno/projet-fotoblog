from blog.models import Photo
from django.forms import Form, ModelForm

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ("image", "caption")