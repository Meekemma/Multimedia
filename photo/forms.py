from django import forms
from django.forms import ModelForm
from .models import *


class PhotoForm(ModelForm):
    class Meta:
        model= Photo
        fields='__all__'

class  CategoryForm(ModelForm):
    class Meta:
        model= Category
        fields='__all__'