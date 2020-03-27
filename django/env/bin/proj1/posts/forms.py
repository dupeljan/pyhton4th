from django import forms
from .models import SpaceObject
class PostForm(forms.ModelForm):
	fields=['idobject','system_idsystem','system_idsystem','type_idtye','name','radius','mass']
	class Meta:
		model = SpaceObject
		fields=['idobject','system_idsystem','system_idsystem','type_idtye','name','radius','mass']

