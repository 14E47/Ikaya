from django import forms

from models import CustomImage

class CustomImageForm(forms.ModelForm):
    class Meta:
        model = CustomImage
        fields = ['name', 'image', 'text', 'text_colour', 'button']