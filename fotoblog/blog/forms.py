from blog.models import Photo, Blog
from django import forms

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("image", "caption")

class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Blog
        fields = ("title", "content")

class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)