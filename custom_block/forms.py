from django import forms

from custom_block.models import CustomImage

class CustomImageForm(forms.ModelForm):
    class Meta:
        model = CustomImage
        fields = ['name', 'image', 'text', 'text_colour', 'button']