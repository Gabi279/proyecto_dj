from django import forms

from .models import Proyectos, ProyectosUsuarios

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Proyectos
        fields = (
            'name',
            'is_active',
        )
        
class ProyectUserForm(forms.ModelForm):
    
    class Meta:
        model = ProyectosUsuarios
        fields = (
            'user',
            'proj_user',
        )
