from django import forms
from .models import ObjectFlat

class ObjectFlatForm(forms.ModelForm):
    class Meta:
        model = ObjectFlat
        fields = ('zone', 'rooms', 'floor', 'wall_material', 'remont', 'parking', 'lift',)
