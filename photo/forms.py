# coding: utf-8

from django import forms
from photo.models import Photo

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image_file', 'description', )
