from django.db import models
from django.conf import settings

from .managers import ProjectsManager

# Create your models here.

class Proyectos(models.Model):
    name = models.CharField('Nombre', max_length=50)
    
    is_active = models.BooleanField(default=False)
    
    objects = ProjectsManager()
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
    
    def __str__(self):
        return str(self.id) + ' - ' + self.name
    
class ProyectosUsuarios(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    proj_user = models.ForeignKey(
        Proyectos, 
        on_delete=models.CASCADE
    )
    
    is_active = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Proyecto User'
        verbose_name_plural = 'Proyecto Users'
    
    def __str__(self):
        return str(self.id) + ' - ' + str(self.user)