from django import forms
from .models import MediaUploaded

class MediaUploadedForm(forms.ModelForm):
    class Meta:
        models = MediaUploaded
        fields = ['title', 'image', 'video']