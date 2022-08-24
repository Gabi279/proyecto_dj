from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)

from .forms import ProjectForm
from .models import Proyectos, ProyectosUsuarios

# Create your views here.

class ProjectView(ListView):
    template_name = "projects/proyectos.html"
    context_object_name = 'projects'
    
    def get_queryset(self):
        lista = Proyectos.objects.all()
        return lista
    
    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context["proyecto"] = Proyectos.objects.all()
        return context
    
class ProjectUserView(ListView):
    template_name = "projects/proj_users.html"
    context_object_name = 'proj_users'
    
    def get_queryset(self):
        lista = ProyectosUsuarios.objects.all()
        return lista
    
    def get_context_data(self, **kwargs):
        context = super(ProjectUserView, self).get_context_data(**kwargs)
        context["proyecto"] = ProyectosUsuarios.objects.all()
        return context
    

class ProyectoCreateView(CreateView):
    template_name = "projects/new_project.html"
    model = Proyectos
    form_class = ProjectForm

    
class ProjectUpdateView(UpdateView):
    template_name = "projects/proj_update.html"
    model = Proyectos
    form_class = ProjectForm
    success_url = reverse_lazy('home_app:home')


class ProjectDeleteView(DeleteView):
    template_name = "projects/proj_delete.html"
    model = Proyectos
    success_url = reverse_lazy('project_app:proyectos')
    
