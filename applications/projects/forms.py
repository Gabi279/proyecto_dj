from django import forms

from .models import Proyectos

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Proyectos
        fields = (
            'name',
        )