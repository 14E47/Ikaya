from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView

from custom_block.models import CustomImage
from custom_block.forms import CustomImageForm

class CustomImageList(ListView):
    model = CustomImage
    template_name = 'custom_block/custom_block_list.html'
    fields = ['name']

class CustomImageCreate(CreateView):
    template_name = 'custom_block/custom_block_create.html'    
    success_url = reverse_lazy('custom-image-list')
    form_class = CustomImageForm
    model = CustomImage

class CustomImageUpdate(UpdateView):
    template_name = 'custom_block/custom_block_update.html'
    success_url = reverse_lazy('custom-image-list')
    form_class = CustomImageForm
    model = CustomImage

class CustomImageDelete(DeleteView):
    template_name = 'custom_block/custom_block_delete.html'
    success_url = reverse_lazy('custom-image-list')
    model = CustomImage