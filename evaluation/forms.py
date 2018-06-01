from django import forms
from .models import Object

class ObjectForm(forms.ModelForm):

    class Meta:
        model = Object
        fields = ('zone', 'rooms', 'floor', 'wall_material', 'remont', 'parking', 'lift',)

